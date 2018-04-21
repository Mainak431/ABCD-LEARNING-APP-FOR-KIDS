from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User

class letters(models.Model):
    id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=1,verbose_name="Enter A letter",null=True)
    correct = models.ImageField(upload_to='pics',verbose_name="Enter the correct Image",null=True)
    correct_name = models.CharField(max_length=20,verbose_name="Upload the name of the correct object",null=True)
    incorrect1 = models.ImageField(upload_to='pics',verbose_name="Upload 1st incorrect Image",null=True)
    incorrect2 = models.ImageField(upload_to='pics',verbose_name="Upload 2nd incorrect Image",null=True)
    incorrect3 = models.ImageField(upload_to='pics',verbose_name="Upload 3rd incorrect Image",null=True)
    Audio = models.FileField(upload_to='songclips',verbose_name="Upload Audio Ex: A for Apple",null=True,blank=True)
    message = models.CharField(max_length=20,verbose_name="Enter the text : Ex: A FOR APPLE",null=True)


