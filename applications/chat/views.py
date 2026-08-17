from django.shortcuts import render, redirect, get_object_or_404
from .models import chat
from .models import user
from .forms import IniciarChatForm
from  django.views import View
from applications.mensaje.models import mensaje


# Create your views here.
  
class IniciarChatView(View):
    template_name = "chat/inichat.html"
    def get(self, request):
        form = IniciarChatForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        user_id = request.session.get("user_id")
        if not user_id:
            return redirect("user_app:login")

        try:
            emisor = user.objects.get(pk=user_id)
        except user.DoesNotExist:
            return redirect("user_app:login")

        form = IniciarChatForm(usuario_emisor=emisor, data=request.POST)
        if form.is_valid():
            receptor = form.cleaned_data["receptor_obj"]
            mensaje_texto = form.cleaned_data["mensaje"]

            
            chat_existente = chat.objects.filter(
                user_idA__in=[emisor, receptor],
                user_idB__in=[emisor, receptor]
            ).first()

            
            if chat_existente:
                if chat_existente.user_idA == emisor and not chat_existente.is_visibleA:
                    chat_existente.is_visibleA = True
                    chat_existente.save()
                    return redirect('mensaje_app:panel_chat', chat_existente.id)
                elif chat_existente.user_idB == emisor and not chat_existente.is_visibleb:
                    chat_existente.is_visibleb = True
                    chat_existente.save()
                    return redirect('mensaje_app:panel_chat', chat_existente.id)
                form.add_error("receptor", "Ya tienes un chat con este usuario.")
                return render(request, self.template_name, {'form': form})

            
            nuevo_chat = chat.objects.create(user_idA=emisor, user_idB=receptor)

            
            mensaje.objects.create(chat=nuevo_chat,content=mensaje_texto,user_id=emisor)

            return redirect("mensaje_app:panel_chat",nuevo_chat.id)  

        return render(request, self.template_name, {'form': form})
    
class DeleteChatView(View):
    def post(self, request, chat_id):
        user_id = request.session.get("user_id")
        current_chat = get_object_or_404(chat, id=chat_id)

        if current_chat.user_idA.id == user_id:
            current_chat.is_visibleA = False
            mensajes = mensaje.objects.filter(chat=current_chat)
            for m in mensajes:
                m.is_visibleA = False
                m.save()
        elif current_chat.user_idB.id == user_id:
            current_chat.is_visibleb = False
            mensajes = mensaje.objects.filter(chat=current_chat)
            for m in mensajes:
                m.is_visibleb = False
                m.save()

        current_chat.save()
        return redirect('mensaje_app:panel')