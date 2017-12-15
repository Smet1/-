from django.contrib import admin
from myapp.models import BankModel, CustomerModel, AccountModel, TransactionsModel


class CustomerAdmin(admin.ModelAdmin):
    exclude = ('password', )
    search_fields = ['idCustomer', 'fio']
    list_display = ('idCustomer', 'get_last_name', 'login')
    list_filter = ['fio']

    pass


# Register your models here.

admin.site.register(BankModel)
admin.site.register(CustomerModel, CustomerAdmin)
admin.site.register(AccountModel)
admin.site.register(TransactionsModel)
