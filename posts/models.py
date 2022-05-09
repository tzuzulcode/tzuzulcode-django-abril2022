from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50,verbose_name="Title")
    description = models.CharField(max_length=100)
    img = models.CharField(max_length=240)
    content = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.created_date.strftime("%d/%m/%Y") + " " + self.title