from django.db import models
# import datetime as dt

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    # date  = models.CharField(max_length=50)


    # This helps the admin to display the name of the model
    def __str__(self):
        return self.name
    
