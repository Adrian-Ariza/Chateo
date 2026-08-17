from .models import user

def user_custom_context(request):
    user_obj = None
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user_obj = user.objects.get(id=user_id)
        except user.DoesNotExist:
            pass
    return {'user_custom': user_obj}
