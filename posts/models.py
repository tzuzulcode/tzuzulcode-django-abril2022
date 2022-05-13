from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50,verbose_name="Title")
    description = models.CharField(max_length=100)
    img = models.CharField(max_length=240)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created_date.strftime("%d/%m/%Y") + " " + self.title

    def get_url(self):
        return reverse('posts:post_detail', args=[self.pk])
