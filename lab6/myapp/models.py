from django.db import models


# Create your models here.


class BankModel(models.Model):
    class Meta:
        db_table = 'banks'

    idBanks = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=16)
    comments = models.CharField(max_length=1000)

    def __str__(self):
        return "name: {}".format(self.name)


class CustomerModel(models.Model):
    class Meta:
        db_table = 'customer'

    idCustomer = models.AutoField(primary_key=True)
    fio = models.CharField(max_length=200)
    login = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=45)
    phone = models.CharField(max_length=16, unique=True)

    def get_last_name(self):
        return self.fio[:-5]
    get_last_name.short_description = 'Last name'

    def __str__(self):
        return "id: {}, fio: {}, login: {}".format(self.idCustomer, self.fio, self.login)


class AccountModel(models.Model):
    class Meta:
        db_table = 'accounts'

    idAccounts = models.AutoField(primary_key=True)
    customerId_FK = models.ForeignKey(
        CustomerModel,
        db_column='customerId_FK'
    )
    bankId_FK = models.ForeignKey(
        BankModel,
        db_column='bankId_FK'
    )
    type = models.CharField(max_length=30)
    money = models.IntegerField()
    currency = models.CharField(max_length=10)

    def __str__(self):
        return "id: {}, fio: {}".format(self.idAccounts, self.customerId_FK.fio)


class TransactionsModel(models.Model):
    class Meta:
        db_table = 'transactions'

    idTransactions = models.AutoField(primary_key=True)

    customerId_from = models.ForeignKey(
        CustomerModel,
        related_name='customerId_from',
        db_column='CustomerId_from'
    )
    customerId_to = models.ForeignKey(
        CustomerModel,
        related_name='customerId_to',
        db_column='CustomerId_to'
    )
    accountId_to = models.ForeignKey(
        AccountModel,
        related_name='accountId_to',
        db_column='AccountId_to'
    )
    accountId_from = models.ForeignKey(
        AccountModel,
        related_name='accountId_from',
        db_column='AccountId_from'
    )

    money = models.IntegerField()
    currency = models.CharField(max_length=10)
    comment = models.CharField(max_length=100)
    time = models.DateField()

    def __str__(self):
        return "id: {}, fio_from: {}, fio_to: {}".format(self.idTransactions, self.customerId_from.fio,
                                                         self.customerId_to.fio)
