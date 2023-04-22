from django.db import models

# Create your models here.

class booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_number = models.IntegerField()
    comment = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.guest_number} guests"

class Menu(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.TextField(max_length=2000)
    img = models.ImageField(blank=True,null=True,upload_to='menu_items/')

    def __str__(self):
        return self.name