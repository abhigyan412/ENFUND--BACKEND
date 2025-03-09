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
