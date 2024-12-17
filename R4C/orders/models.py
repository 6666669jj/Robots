from django.db import models

from customers.models import Customer
from robots.models import Robot

ORDER_STATUS = [
    ('awaiting', 'Ожидает'),
    ('notified', 'Уведомлен'),
    ('completed', 'Доставлен')
]

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    robot_serial = models.CharField(max_length=5, blank=False, null=False)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='awaiting')


