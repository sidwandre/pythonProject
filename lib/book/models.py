from django.db import models

# Create your models here.
class BookDB(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    copies = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title}"