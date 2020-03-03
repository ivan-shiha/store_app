from django.db import models

# Create your models here.

class Animal(models.Model):
    KIND_CHOISES = {
        ('D', 'Dog'),
        ('C', 'Cat')
    }
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=20)
    description = models.TextField()
    image_url = models.URLField()
    kind = models.CharField(max_length=1, choices=KIND_CHOISES)

    def __str__(self):
        return f'{self.name} and I am {self.age}'