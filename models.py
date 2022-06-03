from django.db import models

from django.db.models.signals import post_delete
from django.dispatch import receiver
# Create your models here.

class basic(models.Model):
    ID=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=30)

    def __str__(self):
        return str(self.Name)

class account(models.Model):
    AID = models.IntegerField(primary_key=True)
    Bank_Name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.Bank_Name)

@receiver(post_delete,sender=basic)
def ac_del(sender,instance,**kwargs):
    O=account.objects.get(AID=instance.ID)
    O.delete()
    print("Data is deleted")