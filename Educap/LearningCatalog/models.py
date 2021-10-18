from django.db import models

# Create your models here.


class Category(models.Model):
    Name = models.CharField(max_length=30)
    Description = models.CharField(max_length=100)
    DateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Name}"
