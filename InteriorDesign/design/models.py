from django.db import models

# Create your models here.
class Work(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    story = models.TextField()

def __str__(self):
    return self.name