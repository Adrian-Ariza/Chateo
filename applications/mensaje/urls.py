from django.urls import path
from . import views

app_name = 'mensaje_app'
urlpatterns = [
    
    path("mismensajes/<int:pk>/enviar/", views.SendMensaje.as_view(), name='send_mensaje'),
    path('delchat/<int:pk>/', views.DeleteMensajesView.as_view(), name='delete_mensajes'),
    path("panel/", views.PanelChatView.as_view(), name="panel"),
    path("panel/<int:chat_id>/", views.PanelChatView.as_view(), name="panel_chat"),

]