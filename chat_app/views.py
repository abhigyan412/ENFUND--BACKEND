from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, "chat_app/index.html")
def start_chat(request):
    return JsonResponse({"message": "Chat API working!"})
