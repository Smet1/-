from django.db import models

# Create your models here.


class BankModel(models.Model):
    class Meta:
        db_table = 'banks'
    idBanks = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return "name: {}, 'address': {}".format(self.name, self.address)
