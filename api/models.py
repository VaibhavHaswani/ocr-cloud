from django.db import models

# Create your models here.
class ImgFile(models.Model):
    img=models.ImageField('images/')