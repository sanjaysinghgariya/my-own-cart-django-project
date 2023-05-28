from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")
    additional_info = models.CharField(max_length=5000, default=" ")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    message_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50, default ="")
    phone = models.IntegerField( default ="")
    desc = models.CharField(max_length=300, default ="")

    def __str__(self):
        return self.name

class Orders(models.Model):
    Order_id = models.AutoField(primary_key=True)
    items_jason = models.CharField(max_length=300)
    name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50, default ="")
    phone = models.IntegerField( default ="")
    Address = models.CharField(max_length=50)
    city = models.CharField(max_length=50, default ="")
    State = models.CharField(max_length=10, default ="")
    zip_code = models.IntegerField( default="")


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    Order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    time_stamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "....."

