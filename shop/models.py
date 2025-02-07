from django.db import models

# Create your models here.

# one to one field


# class Person(models.Model):
#     name = models.CharField(max_length=100)

    
#     def __str__(self):
#         return self.name
 

# class Profile(models.Model):
#     person = models.OneToOneField(Person, on_delete=models.CASCADE)
#     bio = models.TextField()


#     def __str__(self):
#         return f"{self.person.name} profile"
    
    
#     class Meta:
#         ordering = ['bio']
    
 

 




# foreign key field many to one
        


class Author(models.Model):
    name1= models.CharField(max_length=100)

    def __str__(self):
        return self.name1



class Book(models.Model):
    title1 = models.CharField(max_length=100)
    author1 = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title1
    


class Department(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name=models.CharField(max_length=70)
    address=models.CharField(max_length=90)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    


class Department1(models.Model):
    name1=models.CharField(max_length=50)

    def __str__(self):
        return self.name1

class Employee1(models.Model):
    name1=models.CharField(max_length=70)
    address1=models.CharField(max_length=90)
    department1=models.ManyToManyField(Department1)

    def __str__(self):
        return self.name1



class BookNew(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    pages=models.IntegerField()

    def __str__(self):
        return self.name






# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.PositiveIntegerField()

#     def __str__(self):
#         return self.name

#     @property
#     def total_price(self):
#         """
#         Calculate the total price of the product based on its price and quantity.
#         """
#         return self.price * self.quantity
    
#     @total_price.setter
#     def total_price(self, value):
#         """
#         Setter method for total_price.
#         """
#         # Setting total_price will update quantity if price is not zero
#         if self.price != 0:
#             self.quantity = value / self.price

    

# zepto models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
    
class ProductCategories(models.Model):
    category_image=models.ImageField(blank=True,null=True,upload_to='images')
    category_name=models.CharField(max_length=50)

    def __str__(self) :
        return self.category_name

@receiver(post_delete, sender=ProductCategories)
def delete_image_file(sender, instance,**kwargs):
    # Delete the associated image file when the model instance is deleted
    if instance.category_image:
        file_path = instance.category_image.path
        if os.path.isfile(file_path):
            os.remove(file_path)
