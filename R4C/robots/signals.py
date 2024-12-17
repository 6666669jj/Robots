from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from orders.models import Order
from .models import Robot

@receiver(post_save, sender=Robot)
def notify_customers_when_robot_created(sender, instance, created, **kwargs):
    """
    Этот сигнал срабатывает при создании нового робота. Если робот добавлен,
    то отправляем уведомления всем клиентам, чьи заказы находятся в статусе 'awaiting'.
    """
    if created:
        # ищем заказы с данным роботом, которые находятся в статусе "Ожидает"
        pending_orders = Order.objects.filter(robot_serial=instance.serial, status='awaiting')

        for order in pending_orders:
            # итправляем уведомление по email
            send_mail(
                subject="Ваш робот теперь в наличии!",
                message=f"Здравствуйте! Ваш заказ на робота модели {instance.model}, версии {instance.version} теперь в наличии.",
                from_email='r4c@gmail.com',  # Замените на ваш реальный email
                recipient_list=[order.customer.email],
            )
            # обновляем статус заказа на "notified"
            order.status = 'notified'
            order.save()
