from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL

class BillingProfile(models.Model):
    user        = models.OneToOneField(User, null=True, blank=True)
    email       = models.EmailField()
    active      = models.BooleanField(default=True)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now=True)
    # costumer_id in Stripe or Briantree

    def __str__(self):
        return self.email

# def billing_profile_creared_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         print("ACTUAL API REQUEST send to stripe/Briantree")
#         instance.costumer_id = newID
#         instance.save()

def user_created_receiver(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_create(user=instance, email=instance.email)

post_save.connect(user_created_receiver, sender=User)
