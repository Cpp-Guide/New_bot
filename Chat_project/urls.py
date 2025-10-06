# Chat_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ Route all root traffic to Chatbot app
    path('', include('Chatbot.urls')),
]