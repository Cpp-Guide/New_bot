from django.urls import path
from .views import chat_view

urlpatterns = [
    path('', chat_view, name='chat'),       # http://127.0.0.1:8000/
    path('chat/', chat_view, name='chat2')  # http://127.0.0.1:8000/chat/
]