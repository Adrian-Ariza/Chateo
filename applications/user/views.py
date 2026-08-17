from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from .forms import UserCreateForm,Loginuser,PasswordChangeForm,EditUserForm
from .models import user
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import check_password,make_password
from django.utils.timezone import now
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

# Create your views here.
class CreateUser(CreateView):
    model=user
    form_class=UserCreateForm
    template_name='user/register.html'
    success_url=reverse_lazy('user_app:login')
  

@method_decorator(ensure_csrf_cookie, name='dispatch')
class Login(FormView):
    template_name = 'user/login.html'
    form_class = Loginuser
    success_url = reverse_lazy('mensaje_app:panel')
    def form_valid(self, form):
        userName = form.cleaned_data.get('userName')
        password = form.cleaned_data.get('password')
        try:
            user_obj = user.objects.get(userName=userName)
        except user.DoesNotExist:
            form.add_error(None, "Usuario no encontrado")
            return self.form_invalid(form)
        if check_password(password, user_obj.password):
            if(user_obj.is_visble):
                user_obj.isActive=True
                user_obj.save()
                self.request.session['user_id'] = user_obj.id
                return redirect(self.get_success_url())
            else:
                form.add_error(None, "Usuario no existe")
                return self.form_invalid(form)
        else:
            form.add_error(None, "Contraseña incorrecta")
            return self.form_invalid(form)
        
def logout_user(request):
    user_id = request.session.get("user_id")
    if user_id is not None:
        try:
            user_obj = user.objects.get(pk=user_id)
            user_obj.LastSignDate = now()
            user_obj.isActive = False 
            user_obj.save()
        except user.DoesNotExist:
            pass
    
    request.session.flush()  
    return redirect('user_app:Home')

class GoHome(TemplateView):
    template_name='home/home.html'  

class MiPorfile(TemplateView):
    template_name='user/miporfile.html' 

class editUser(UpdateView):
    model = user
    form_class = EditUserForm
    template_name = 'user/userUpd.html'
    success_url = reverse_lazy('user_app:miporfile')

    def get_object(self, queryset=None):
        user_id = self.request.session.get("user_id")
        return user.objects.get(pk=user_id)

class ChangePasswordView(FormView):
    template_name = 'user/chgpass.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('mensaje_app:miporfile')
    def form_valid(self, form):
        user_id = self.request.session.get("user_id")
        if not user_id:
            form.add_error(None, "Sesión no válida.")
            return self.form_invalid(form)
        try:
            user_obj = user.objects.get(id=user_id)
        except user.DoesNotExist:
            form.add_error(None, "Usuario no encontrado.")
            return self.form_invalid(form)
        current_password = form.cleaned_data['current_password']
        new_password = form.cleaned_data['new_password']

        if not check_password(current_password, user_obj.password):
            form.add_error("current_password", "La contraseña actual es incorrecta.")
            return self.form_invalid(form)

        if len(new_password) < 8:
            form.add_error("new_password", "La nueva contraseña debe tener al menos 8 caracteres.")
            return self.form_invalid(form)

        user_obj.password = make_password(new_password)
        user_obj.save()
        return redirect(self.get_success_url())
    
class DeleteUserView(View):
    def post(self, request):
        user_id = request.session.get("user_id")
        if not user_id:
            return redirect("user_app:login") 

        try:
            user_obj = user.objects.get(id=user_id)
            user_obj.is_visble = False
            user_obj.isActive=False
            user_obj.LastSignDate=now()
            user_obj.save()

            request.session.flush()

            return redirect("user_app:login")  
        except user.DoesNotExist:
            return redirect("user_app:login")