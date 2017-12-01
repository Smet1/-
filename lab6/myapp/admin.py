from django.contrib import admin
from myapp.models import BankModel, CustomerModel, AccountModel, TransactionsModel

# Register your models here.

admin.site.register(BankModel)
admin.site.register(CustomerModel)
admin.site.register(AccountModel)
admin.site.register(TransactionsModel)
