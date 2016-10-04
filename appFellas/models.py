from django.db import models


class User(models.Model):
    e_mail = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)


class Image(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='author', default='')
    uploaded = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='')


