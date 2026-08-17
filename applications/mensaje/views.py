from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from applications.chat.models import chat
from applications.mensaje.models import mensaje
from applications.user.models import user
from .forms import MensajeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.db.models import Max


class SendMensaje(CreateView):
    model = mensaje
    form_class = MensajeForm
    template_name = 'mensaje/panel_chat.html'

    def form_valid(self, form):
        chat_obj = chat.objects.get(pk=self.kwargs['pk'])  
        form.instance.chat = chat_obj

        user_id = self.request.session.get('user_id')
        form.instance.user_id = user.objects.get(pk=user_id)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('mensaje_app:panel_chat', kwargs={'chat_id': self.kwargs['pk']})


class DeleteMensajesView(View):
    def post(self, request, pk):
        user_id = request.session.get("user_id")
        chat_obj = get_object_or_404(chat, id=pk)

        mensajes_chat = mensaje.objects.filter(chat=chat_obj)

        for m in mensajes_chat:
            if m.user_id.id == chat_obj.user_idA.id and user_id == chat_obj.user_idA.id:
                m.is_visibleA = False
                m.save()
            elif m.user_id.id == chat_obj.user_idB.id and user_id == chat_obj.user_idB.id:
                m.is_visibleb = False
                m.save()
        return redirect('mensaje_app:panel')
    
class PanelChatView(View):
    def get(self, request, chat_id=None):
        user_id = request.session.get("user_id")
        if not user_id:
            return redirect("user_app:login")

        current_user = get_object_or_404(user, id=user_id)
        chats = current_user.chats_as_userA.all() | current_user.chats_as_userB.all()
        chats = chats.annotate(
    last_message_date=Max('mensaje__sendDate')
).order_by('-last_message_date')

        selected_chat = None
        mensajes = []
        form = MensajeForm()
        can_send_message = False

        if chat_id:
            selected_chat = get_object_or_404(chat, id=chat_id)
            mensajes = mensaje.objects.filter(chat=selected_chat).order_by("sendDate")
            
            
            mensajes.filter(is_read=False).exclude(user_id_id=user_id).update(is_read=True)

            
            if (selected_chat.user_idA.id == user_id and selected_chat.is_visibleA and not selected_chat.is_bloquedA) or \
               (selected_chat.user_idB.id == user_id and selected_chat.is_visibleb and not selected_chat.is_bloquedB):
                can_send_message = True

        context = {
            "user_custom": current_user,
            "chats": chats,
            "chat": selected_chat,
            "mensajes": mensajes,
            "form": form,
            "can_send_message": can_send_message,
        }
        return render(request, "mensaje/panel_chat.html", context)
