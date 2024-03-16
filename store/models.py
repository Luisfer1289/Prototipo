from django.db import models
from usuarios.models import CustomUser

# Create your models here.


	
class Product(models.Model):
	name = models.CharField(max_length=200, null=True)
	price = models.DecimalField(max_digits=7, decimal_places=2)
	digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(upload_to='products', blank=False, default='products/producto_defecto.png')
	description = models.TextField(null=True, blank=True) 
    
	def __str__(self):
		return self.name
	
	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	
	
class Order(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, default=1)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False, null=True, blank=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
	
	@property
	def shipping(self): 
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems: 
			if i.product.digital == False:
				shipping = True
		return shipping 


	@property	
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total
	
	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total  = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, default=1)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,  blank=True) 
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address