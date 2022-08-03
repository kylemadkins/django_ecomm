from django.db import models

class Collection(models.Model):
  title = models.CharField(max_length=255)

class Product(models.Model):
  sku = models.CharField(max_length=255, primary_key=True)
  title = models.CharField(max_length=255)
  description = models.TextField()
  price = models.DecimalField(max_digits=6, decimal_places=2)
  inventory = models.IntegerField()
  collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
  updated_at = models.DateTimeField(auto_now=True)

class Customer(models.Model):
  BRONZE = 'B'
  SILVER = 'S'
  GOLD = 'G'
  MEMBERSHIP_CHOICES = [
    (BRONZE, 'Bronze'),
    (SILVER, 'Silver'),
    (GOLD, 'Gold')
  ]
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  phone = models.CharField(max_length=50)
  date_of_birth = models.DateField(null=True)
  membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=BRONZE)

class Address(models.Model):
  street = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Order(models.Model):
  PENDING = 'P'
  COMPLETE = 'C'
  FAILED = 'F'
  STATUS_CHOICES = [
    (PENDING, 'Pending'),
    (COMPLETE, 'Complete'),
    (FAILED, 'Failed')
  ]
  created_at = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING)
  customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class OrderItem(models.Model):
  order = models.ForeignKey(Order, on_delete=models.PROTECT)
  product = models.ForeignKey(Product, on_delete=models.PROTECT)
  quantity = models.PositiveSmallIntegerField()
  unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Cart(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveSmallIntegerField()
