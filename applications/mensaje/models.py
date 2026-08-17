from django.db import models

from applications.user.models import user
from applications.chat.models import chat

# Create your models here.
class mensaje(models.Model):
    chat=models.ForeignKey(chat,on_delete=models.DO_NOTHING)
    content=models.CharField(max_length=500,null=False)
    sendDate=models.DateTimeField(null=False,auto_now_add=True)
    user_id=models.ForeignKey(user,on_delete=models.DO_NOTHING)
    is_read=models.BooleanField(default=False,null=False)
    is_visibleA=models.BooleanField(default=True,null=False)
    is_visibleb=models.BooleanField(default=True,null=False)

    def __str__(self):
        return str(self.id)+"-"+self.content+"-"+str(self.sendDate)+"-"+str(self.chat)+"-"+str(self.user_id)