from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from myapp.models import BankModel, CustomerModel, AccountModel, TransactionsModel
from myapp.forms import *


# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'main.html')


class Bank(View):
    def get(self, request):
        data = BankModel.objects.all()
        return render(request, 'banks_main.html', {'banks': data})


class BankInDetail(View):
    def get(self, request, id):
        data = BankModel.objects.get(idBanks=int(id))
        '''data_out = {
            'banks': {
                'id': id,
                'name': data.name,
                'address': data.address
            }
        }'''
        return render(request, 'bank_detail.html', {'banks': data})


class Customer(View):
    def get(self, request):
        data_cus = CustomerModel.objects.all()
        return render(request, 'customer_main.html', {'customers': data_cus})


class CustomerInDetail(View):
    def get(self, request, id):
        data = CustomerModel.objects.get(idCustomer=int(id))
        data1 = AccountModel.objects.filter(customerId_FK=int(id))
        data2 = TransactionsModel.objects.filter(customerId_from=int(id))
        return render(request, 'customer_detail.html', {'customers': data, 'accts': data1, 'trans': data2})


class CustomerAccounts(View):
    def get(self, request):
        data = AccountModel.objects.all()
        return render(request, 'accounts_main.html', {'accts': data})


class CustomerTransactions(View):
    def get(self, request):
        data = TransactionsModel.objects.all()
        return render(request, 'transactions_main.html', {'trans': data})


def registration1(request):
    errors = []
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors.append('Введите логин')
        elif len(username) < 4:
            errors.append('Длина пароля должна быть >=4')

        password = request.POST.get('password')
        if not password:
            errors.append('Введите пароль')
        elif len(password) < 3:
            errors.append('Длина пароля должна быть >=3')
        password_repeat = request.POST.get('password2')

        if password != password_repeat:
            errors.append('Пароли не совпадают')

        if not errors:

            return HttpResponseRedirect('/login/')

        return render(request, 'registration.html', {'errors': errors})


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/login/')

    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})


class vlog(View):
    def get(self, request):
        return render(request, 'login.html')

