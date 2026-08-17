
from django.db import models

# Create your models here.


# Cargar configuración directamente desde tu JSON


class user(models.Model):
    name=models.CharField(max_length=30, null=False)
    userName=models.CharField(max_length=30,null=False,unique=True)
    email=models.EmailField(max_length=50,null=False,unique=True)
    picture=models.ImageField(upload_to='usersPic/', default='default/profile-icon.webp',null=True,blank=True)
    password=models.CharField(max_length=200,null=False)
    creationDate=models.DateTimeField(null=False,auto_now_add=True)
    isActive=models.BooleanField(default=False,null=False)
    LastSignDate=models.DateTimeField(auto_now_add=True,null=False)
    is_visble=models.BooleanField(default=True,null=False)

    def __str__(self):
        return str(self.id)+"-"+self.name+"-"+self.userName+"-"+self.email+"-"+str(self.creationDate)+"-"+str(self.isActive)+"-"+str(self.LastSignDate)
   
