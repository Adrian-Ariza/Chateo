from django.urls import path
from . import views

app_name='user_chats'
urlpatterns = [
    
    path('newchat', views.IniciarChatView.as_view(), name='new_chat'),
    path('deletechat/<int:chat_id>/', views.DeleteChatView.as_view(), name='delete_chat')

]