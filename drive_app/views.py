from django.shortcuts import render
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from django.http import JsonResponse
import requests
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
def get_drive_service(access_token):
    creds = Credentials(token=access_token)
    return build("drive", "v3", credentials=creds)


from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build
import os

def refresh_access_token(refresh_token):
    """Refresh Google OAuth access token using the refresh token"""
    token_data = {
        "client_id": settings.GOOGLE_CLIENT_ID,
        "client_secret": settings.GOOGLE_CLIENT_SECRET,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
    }
    response = requests.post("https://oauth2.googleapis.com/token", data=token_data).json()
    return response.get("access_token")

@csrf_exempt
def upload_file(request):
    """Upload a file to Google Drive"""
    try:
        if request.method != "POST":
            return JsonResponse({"error": "Only POST requests allowed"}, status=405)

        access_token = request.headers.get("Authorization")
        if not access_token or "Bearer" not in access_token:
            return JsonResponse({"error": "Missing or invalid access token"}, status=401)

        access_token = access_token.replace("Bearer ", "")

        # Authenticate Google Drive API
        creds = Credentials(token=access_token)
        if creds.expired and creds.refresh_token:
            new_access_token = refresh_access_token(creds.refresh_token)
            creds = Credentials(token=new_access_token)
        drive_service = build("drive", "v3", credentials=creds)

        # Example File Path (Change this to a real file)
        file_path = "test_upload.txt"  # 🔹 Change this to an actual file path
        with open(file_path, "w") as f:
            f.write("Hello from Django!")  # 🔹 Create a test file for upload

        file_metadata = {"name": os.path.basename(file_path)}
        media = MediaFileUpload(file_path, mimetype="text/plain")

        # Upload file to Google Drive
        file = drive_service.files().create(body=file_metadata, media_body=media).execute()

        return JsonResponse({"message": "File uploaded successfully", "file_id": file["id"]})

    except Exception as e:
        return JsonResponse({"error": "Internal Server Error", "details": str(e)}, status=500)




@csrf_exempt
def list_files(request):
    """Fetch a list of files from Google Drive"""
    access_token = request.session.get("access_token")  

    if not access_token:
        return JsonResponse({"error": "User not authenticated with Google Drive"}, status=401)

    headers = {"Authorization": f"Bearer {access_token}"}
    files_url = "https://www.googleapis.com/drive/v3/files"

    response = requests.get(files_url, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json())  
    else:
        return JsonResponse({"error": "Failed to fetch files", "details": response.json()}, status=400)


from django.http import HttpResponse
@csrf_exempt
def download_file(request, file_id):
    """Download a file from Google Drive"""

    
    print("DEBUG: Session Data at /drive/download/ ->", dict(request.session.items()))

    
    access_token = request.session.get("access_token")

    if not access_token:
        return JsonResponse({"error": "User not authenticated with Google Drive"}, status=401)

    print(f"DEBUG: Using Access Token -> {access_token}") 

    
    headers = {"Authorization": f"Bearer {access_token}"}
    download_url = f"https://www.googleapis.com/drive/v3/files/{file_id}?alt=media"

    response = requests.get(download_url, headers=headers, stream=True)

    print(f"DEBUG: Google API Response Code -> {response.status_code}")  

    if response.status_code == 200:
        response_content = response.raw.read()
        response_headers = response.headers.get("Content-Type", "application/octet-stream")
        return HttpResponse(response_content, content_type=response_headers)
    else:
        print(f"DEBUG: Google API Response Content -> {response.text}")  #
        return JsonResponse({"error": "Failed to download file", "details": response.json()}, status=response.status_code)




from django.http import JsonResponse

def debug_session(request):
    """Returns the current session data for debugging"""
    return JsonResponse({"session_data": dict(request.session.items())})
