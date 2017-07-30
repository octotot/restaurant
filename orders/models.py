from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    CITY_CHOICES = (
        (0, 'Москва'),
        (1, 'Санкт-Петербург'),
    )
    name = models.CharField('Название ресторана', max_length=100)
    city = models.PositiveSmallIntegerField('Город', choices=CITY_CHOICES)

    class Meta:
        unique_together = ('name', 'city',)
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'

    def __str__(self):
        return self.name

class DishCategory(models.Model):
    name = models.CharField('Название категории', max_length=50, unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        full_path = [self.name]
        p = self.parent
        
        while p is not None:
            full_path.append(p.name)
            p = p.parent

        return ' -> '.join(full_path[::-1])


class Dish(models.Model):
    name = models.CharField('Название блюда', max_length=100, unique=True)
    price = models.PositiveIntegerField('Цена')
    category = models.ForeignKey(DishCategory, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.name

class Order(models.Model):
    price = models.PositiveIntegerField('Цена')
    operator = models.ForeignKey(User, on_delete=models.PROTECT)
    time = models.DateTimeField(auto_now_add=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
    STATUS_CHOICES = (
        (0, 'Принят'),
        (1, 'Оплачен'),
        (2, 'Исполнен'),
        (3, 'Отменен')
    )
    status = models.PositiveSmallIntegerField('Статус', default=0, choices=STATUS_CHOICES)

    def save(self, *args, **kwargs):
        self.price = 0
        for item in self.items:
            self.price += item.price
        super(OrderItem, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class OrderItem(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.PROTECT)
    count = models.PositiveIntegerField('Количество')
    price = models.PositiveIntegerField('Цена', editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')

    def save(self, *args, **kwargs):
        self.price = self.dish.price
        super(OrderItem, self).save(*args, **kwargs)
