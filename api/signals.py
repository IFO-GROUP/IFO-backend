from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models import Subscriber
from api.tasks import send_mail


@receiver(post_save, sender= Subscriber)
def send_subscriber_email(sender, instance, created, **kwargs):
    if created:
        send_mail(instance) 
        
        