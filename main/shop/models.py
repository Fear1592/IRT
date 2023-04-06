from django.db import models

from product.models import Choices
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    paid = models.BooleanField(default=False, verbose_name='Статус оплаты')

    class Meta:
        ordering = ['-created']
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


    def get_total_price(self):
        total = sum(item.get_cost() for item in self.order.all())
        return total

    def __str__(self):
        return f'{self.get_total_price()}'




class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    choices = models.ForeignKey(Choices, on_delete=models.CASCADE, related_name='choices')
    quantity = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ['-id']
        verbose_name = "Товар в заказ"
        verbose_name_plural = "Товары в заказах"




    def get_cost(self):
        return self.choices.price * self.quantity



    def __str__(self):
        return str(self.get_cost())
