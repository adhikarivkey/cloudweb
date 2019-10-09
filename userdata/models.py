from django.db import models
from django.contrib.auth.models import User


class UserDataDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=128,blank=False)
    description = models.TextField(max_length=400, blank=True, null=True)
    image = models.FileField(upload_to= 'photos')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class MultipleImg(models.Model):
    name = models.ForeignKey(UserDataDetail,on_delete=models.CASCADE)
    picture = models.FileField(upload_to= 'photos',blank=True,null=True)


    def __str__(self):
        return self.name.user