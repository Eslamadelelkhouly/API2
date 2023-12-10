from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=300,default="",blank=False)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20,default="",blank=True)
    password = models.CharField(max_length=20,default="",blank=False)


class Book(models.Model):
    book_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=300,default="",blank=False)
    image = models.CharField(max_length=700,default="",blank=False)
    price = models.IntegerField()
    author_name = models.CharField(max_length=250,default="",blank=False)
    rating = models.DecimalField(max_digits=3,decimal_places=2,default=0)