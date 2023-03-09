from django.db import models

class Post(models.Model):

    title = models.CharField(verbose_name="Name", max_length=100)
    discription = models.TextField(verbose_name='Description', null=True)
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updated at', auto_now=True)
    image = models.ImageField(verbose_name='Image', )

    def __str__(self):
        return f'{self.title}'

