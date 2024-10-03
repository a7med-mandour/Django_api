from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    created_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.name