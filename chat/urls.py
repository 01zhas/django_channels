from django.urls import path

from chat import views

urlpatterns = [
    path('', views.chat_room, name='chat_room'),
]
