from django.db import models

from applications.user.models import user

# Create your models here.
class chat(models.Model):
    user_idA=models.ForeignKey(user,on_delete=models.DO_NOTHING, related_name='chats_as_userA')
    user_idB=models.ForeignKey(user,on_delete=models.DO_NOTHING, related_name='chats_as_userB')
    is_bloquedA=models.BooleanField(default=False,null=False)
    is_bloquedB=models.BooleanField(default=False,null=False)
    is_visibleA=models.BooleanField(default=True,null=False)
    is_visibleb=models.BooleanField(default=True,null=False)
    

    def __str__(self):
        return str(self.id)+"-"+str(self.user_idA)+"-"+str(self.user_idB)
   