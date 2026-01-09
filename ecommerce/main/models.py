from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='products/')
    stock=models.IntegerField()
    category=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Order(models.Model):
    #if user delete account all orders deleted automatically
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    total_price=models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
