from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

CITY_CHOICES = (
    (0, 'Moscow'),
    (1, 'Saint Petersburg'),
)

STATUS_CHOICES = (
    (0, 'Accepted'),
    (1, 'Paid'),
    (2, 'Completed'),
    (3, 'Cancelled')
)

class Restaurant(models.Model):   
    name = models.CharField('Restaurant Name', max_length=100)
    city = models.PositiveSmallIntegerField('City', choices=CITY_CHOICES)

    class Meta:
        unique_together = ('name', 'city',)
    
    def __str__(self):
        return self.name + ' in ' + CITY_CHOICES[self.city][1]

class DishCategory(models.Model):
    name = models.CharField('Category Name', max_length=50, unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='subcategories')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        full_path = [self.name]
        p = self.parent
        
        while p is not None:
            full_path.append(p.name)
            p = p.parent

        return ' -> '.join(full_path[::-1])

    class JSONAPIMeta:
        resource_name = 'category'

class Dish(models.Model):
    name = models.CharField('Dish Name', max_length=100, unique=True)
    price = models.PositiveIntegerField('Price')
    category = models.ForeignKey(DishCategory, on_delete=models.PROTECT, related_name='dishes')

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'

    def __str__(self):
        return self.name

    class JSONAPIMeta:
        resource_name = 'dish'

class Order(models.Model):
    price = models.PositiveIntegerField('Price')
    operator = models.ForeignKey(User, on_delete=models.PROTECT)
    time = models.DateTimeField(auto_now_add=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField('Status', default=0, choices=STATUS_CHOICES)

    def __str__(self):
        s = ''
        for item in self.items.all():
            s += ', ' +  str(item)
        return s[2:]

    class JSONAPIMeta:
        resource_name = 'order'

class OrderItem(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.PROTECT)
    count = models.PositiveIntegerField('Count')
    price = models.PositiveIntegerField('Price', editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')

    def save(self, *args, **kwargs):
        self.price = self.dish.price
        super(OrderItem, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.count) + ' ' + self.dish.name + ' for ' + str(self.dish.price)
