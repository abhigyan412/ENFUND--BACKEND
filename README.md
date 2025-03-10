#  ENFUND Backend

## Overview

A Django-based backend service deployed on Render, integrating **Google OAuth, Google Drive API, and WebSockets for real-time chat.**  


## Features

-  Google OAuth 2.0 Authentication  
-  Google Drive File Upload & Download  
-  Real-Time Chat with WebSockets  
-  Django REST Framework APIs 
## Technologies Used

- **Backend:** Python, Django, Django REST Framework  
- **Authentication:** Google OAuth 2.0  
- **Storage:** Google Drive API  
- **Real-time Communication:** Django Channels (WebSockets)  
- **Database:** PostgreSQL (Hosted on Render)  
- **Hosting:** Render  
##  Local Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/abhigyan412/ENFUND--BACKEND.git
    cd ENFUND--BACKEND
2. **Create a virtual environment:**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate


3. **Install Dependencies**

     ```bash
     pip install -r requirements.txt

4. **Setup Environment Variables**

   ```bash
   SECRET_KEY=your_secret_key
   DEBUG=False
   GOOGLE_CLIENT_ID=your_google_client_id
   GOOGLE_CLIENT_SECRET=your_google_client_secret

5. **Run Migrations & Start Server**

   ```bash
   python manage.py migrate
   python manage.py runserver




##  API Endpoints
1. **Google OAuth Authentication:**
    ```bash
    /auth/login/	GET	Redirects to Google OAuth login
    /auth/callback/	GET	Handles OAuth callback and returns user data
2. **Google Drive Integration:**
    ```bash
    /drive/upload/	POST	Uploads a file to Google Drive
    /drive/download/<file_id>/	GET	Downloads a file from Google Drive
3. **Real-Time Chat (WebSocket):**
    ```bash
    /ws/chat/<room_name>/	WebSocket	Connects users to a real-time chat room
## 🛠️ Testing the API
You can test the API using **Postman** or **cURL**.

### **1️⃣ Google OAuth Authentication**
#### **Login via Google OAuth**
- **Request:**
  ```bash
  GET https://enfund-backend.onrender.com/auth/login/
 - **Reponse:**
     ```bash
     
   "message": "Redirecting to Google OAuth"
     
    
**OAuth Callback**
  - **Request:**
     ```bash
     GET https://enfund-backend.onrender.com/auth/login/
  - **Reponse:**
      ```bash     
       "email": "user@example.com",
       "name": "John Doe",
       "picture": "profile_image_url",
       "access_token": "ya29.a0AeX..."
        


### **2️⃣Google Drive Integration**
#### **Download a File**
- **Request:**
  ```bash
  GET https://enfund-backend.onrender.com/drive/download/<file_id>/
  Headers:
  Authorization: Bearer <your_access_token>

 - **Reponse:**
    ```bash
       "message": "File downloaded successfully"
       

    
**Upload a File**
  - **Request:**
     ```bash
       POST https://enfund-backend.onrender.com/drive/upload/
       Headers:
       Authorization: Bearer <your_access_token>
       Body (Multipart/Form-Data):
       file: <your_file>

  - **Reponse:**
    ```bash
    
     "message": "File uploaded successfully",
     "file_id": "1B2M2Y8AsgTpgAmY7Ph..."
    

### **3️⃣ WebSockets for Real-Time Chat**
#### **Connect using a WebSocket client like Postman or a browser-based WS tester:**
             ws://enfund-backend.onrender.com/ws/chat/<room_name
**To use on web browser directly :**
             https://enfund-backend.onrender.com/chat/       
**Send a JSON message:**
          ```bash
           "message": "Hello, World!",
           "username": "John"
   


- **Reponse:**
    ```bash
     
      "message": "Hello, World!",
      "username": "John"
        

