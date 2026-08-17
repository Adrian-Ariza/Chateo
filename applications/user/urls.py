from django.urls import path
from . import views

app_name='user_app'
urlpatterns = [
  path('register',views.CreateUser.as_view(),name='register'),
  path('login',views.Login.as_view(),name='login'),
  path('logout', views.logout_user, name='logout'),
  path('home',views.GoHome.as_view(), name="Home"),
  path('edit', views.editUser.as_view(), name='editar_perfil'),
  path('chgpass', views.ChangePasswordView.as_view(), name='change_password'),
  path('deleteuser', views.DeleteUserView.as_view(), name='delete_user'),
  path('miporfile',views.MiPorfile.as_view(), name='miporfile')
]
