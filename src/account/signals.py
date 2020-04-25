from django.db.models.signals import pre_save
from django.dispatch import receiver

import string

from account.models import User


@receiver(pre_save, sender=User)
def pre_save_user(sender, instance, **kwargs):
    instance.email = instance.email.lower()
    instance.first_name = string.capwords(instance.first_name)
    instance.last_name = string.capwords(instance.last_name)
    instance.telephone = ''.join(x for x in instance.telephone if x.isdigit())

    if instance.id is None:
        print('Object is created!')