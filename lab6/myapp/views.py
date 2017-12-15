from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from myapp.models import BankModel, CustomerModel, AccountModel, TransactionsModel
from myapp.forms import UserRegistrationForm, UserAuthenticationForm


def user_type(request):
    if not request.user.is_authenticated:
        usr_type = ''
        usr_id = ''
    else:
        usr_type = request.user
        usr_id = CustomerModel.objects.get(login=usr_type)

    print('data: {}, usr_id: {}'.format(usr_type, usr_id))
    return usr_type, usr_id


# Create your views here.
class Home(View):
    def get(self, request):
        data, usr_id = user_type(request)
        return render(request, 'main.html', {'usr_type': data, 'usr_id': usr_id})


class Bank(View):
    def get(self, request):
        data = BankModel.objects.all()
        usr_type, usr_id = user_type(request)
        return render(request, 'banks_main.html', {'banks': data, 'usr_type': usr_type, 'usr_id': usr_id})


class BankInDetail(View):
    def get(self, request, id):
        data = BankModel.objects.get(idBanks=int(id))
        usr_type, usr_id = user_type(request)
        return render(request, 'bank_detail.html', {'banks': data, 'usr_type': usr_type, 'usr_id': usr_id})


class Customer(View):
    def get(self, request):
        data_cus = CustomerModel.objects.all()
        usr_type, usr_id = user_type(request)
        return render(request, 'customer_main.html', {'customers': data_cus, 'usr_type': usr_type, 'usr_id': usr_id})


class CustomerInDetail(View):
    def get(self, request, id):
        data = CustomerModel.objects.get(idCustomer=int(id))
        data1 = AccountModel.objects.filter(customerId_FK=int(id))
        data2 = TransactionsModel.objects.filter(customerId_from=int(id))
        usr_type, usr_id = user_type(request)
        return render(request, 'customer_detail.html', {'customers': data, 'accts': data1, 'trans': data2,
                                                        'usr_type': usr_type, 'usr_id': usr_id})


class CustomerAccounts(View):
    def get(self, request):
        usr_type, usr_id = user_type(request)
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/auth/')
        else:
            data = AccountModel.objects.all()
            return render(request, 'accounts_main.html', {'accts': data, 'usr_type': usr_type, 'usr_id': usr_id})


class CustomerTransactions(View):
    @method_decorator(login_required(login_url='/auth/'))
    def get(self, request):
        usr_type, usr_id = user_type(request)
        data = TransactionsModel.objects.all()
        return render(request, 'transactions_main.html', {'trans': data, 'usr_type': usr_type, 'usr_id': usr_id})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/home/')


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


# TODO при необходимости заменить функции ниже на классы (декораторы будут исп по-другому и dispatch)

def reg_view(request):  # регистрация
    form = UserRegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)

            user = User.objects.create_user(username=request.POST.get('login'), password=request.POST.get('password'),
                                            last_name=request.POST.get('fio'))

            #  user.first_name = request.POST.get('fio')
            user.save()
            return HttpResponseRedirect('/auth/')

    else:
        form = UserRegistrationForm()

    return render(request, 'registration.html', {'form': form})


def auth_view(request):  # авторизация
    errors = []
    if request.method == 'POST':
        form = UserAuthenticationForm(request.POST)
        print('check valid')

        if form.is_bound:
            print('form is valid', request.POST.get('login'), request.POST.get('password'))

            try:
                print('trying to get data')

                bd_data = CustomerModel.objects.get(login=request.POST.get('login'))

                print('получил бд', bd_data)

                if request.POST.get('password') == bd_data.password:
                    print('авторизация этого пользователя')

                    user = authenticate(username=request.POST.get('login'), password=request.POST.get('password'))
                    print('success - ', user)
                    login(request, user)
                    return HttpResponseRedirect('/home/')

                else:
                    errors.append('неправильный пароль')

            except CustomerModel.DoesNotExist:
                errors.append('неправильный логин')

    else:
        form = UserAuthenticationForm()

    # print(form.errors.as_data())
    print(errors)
    return render(request, 'authentication.html', {'form': form, 'errors': errors})





