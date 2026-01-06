from django.db import models

# Create your models here.
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField()
    stock=models.IntegerField()
    image=models.ImageField(upload_to='product/')
    Created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

