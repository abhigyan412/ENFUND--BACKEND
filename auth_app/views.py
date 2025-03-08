from django.shortcuts import render

from django.shortcuts import redirect
from django.http import JsonResponse
import requests
from django.conf import settings

from django.shortcuts import redirect
from django.conf import settings

def google_login(request):
    auth_url = (
        f"https://accounts.google.com/o/oauth2/auth?"
        f"response_type=code"
        f"&client_id={settings.GOOGLE_CLIENT_ID}"
        f"&redirect_uri={settings.GOOGLE_REDIRECT_URI}"
        f"&scope=openid email profile https://www.googleapis.com/auth/drive.file"
        f"&access_type=offline"
        f"&prompt=consent"
    )
    return redirect(auth_url)




import requests
from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import User

import requests
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.conf import settings

def google_callback(request):
    """Handles Google OAuth callback and logs in the user"""
    code = request.GET.get("code")
    if not code:
        return JsonResponse({"error": "Authorization code not provided"}, status=400)

    token_data = {
        "code": code,
        "client_id": settings.GOOGLE_CLIENT_ID,
        "client_secret": settings.GOOGLE_CLIENT_SECRET,
        "redirect_uri": settings.GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }

    token_response = requests.post("https://oauth2.googleapis.com/token", data=token_data).json()

    if "access_token" not in token_response:
        return JsonResponse({"error": "Failed to obtain access token", "details": token_response}, status=400)

    headers = {"Authorization": f"Bearer {token_response['access_token']}"}
    user_info = requests.get("https://www.googleapis.com/oauth2/v1/userinfo", headers=headers).json()

    if "email" not in user_info:
        return JsonResponse({"error": "Failed to retrieve user info"}, status=400)

    request.session["user_email"] = user_info["email"]
    request.session["access_token"] = token_response["access_token"]

    print("DEBUG: Session after login ->", dict(request.session.items()))  

    return JsonResponse({
        "email": user_info["email"],
        "name": user_info.get("name"),
        "picture": user_info.get("picture"),
        "access_token": token_response["access_token"]
    })
