from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from django.db.models import F, Sum
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
STATE_CHOICES=(
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarath', 'Gujarath'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttarakhand', 'Uttarakhand'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('West Bengal', 'West Bengal'),
)
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)

    def __str__(self):
        return str(self.name)

CATEGORY_CHOICE = (
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('TW', 'Top Wear'),
    ('BW', 'Bottom Wear')
)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=10)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.title)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    # @property
    # def last_cost(self):
    #     import pdb;pdb.set_trace()
    #     # prod = Product.instance
    #     for p in Product:
    #         print(p)
    #     return self.quantity * self.product[2].discounted_pric

    
    # @property
    # def total_price(self):
    #     return self.cartitem_set.aggregate(
    #         total_price=Sum(F('quantity') * F('product__price'))
    #     )['total_price'] or Decimal('0')
    @property
    def last_cost(self):
        # import pdb;pdb.set_trace()
        return self.quantity * self.product.values('discounted_price').get().get("discounted_price")

STATUS_CHOICE = (
    ('Accepted', 'Accepted'),
    ('packed', 'packed'),
    ('On the way', 'On the way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default='Pending')

    @property
    def last_cost(self):
        # import pdb;pdb.set_trace()
        # return self.quantity * list(self.product.values_list('discounted_price', flat=True))[0]
        list1 = list(self.product.values_list('discounted_price', flat=True))
        pri = []
        for x in list1:
            pri.append(self.quantity * x)
        return pri
        # return self.quantity * self.product.values('discounted_price').get().get("discounted_price")

    def __str__(self):
         return (self.customer.name+"_"+str(self.quantity))# +"_"+self.product.values('title').get().get("title")   