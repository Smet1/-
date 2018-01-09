from django import forms
from .models import CustomerModel, TransactionsModel
import datetime


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        exclude = []
    fio = forms.CharField(label='ФИО',)
    phone = forms.CharField(label='Телефон',)
    login = forms.CharField(min_length=4, label='Логин')
    password = forms.CharField(min_length=3, widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(min_length=3, widget=forms.PasswordInput, label='Повторите пароль')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['fio'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите ФИО'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите Ваш номер телефона'})
        self.fields['login'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите Логин'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Повторите пароль'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Пароль'})


class UserAuthenticationForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        #  exclude = ['fio', 'phone']
        fields = ['login', 'password']

    login = forms.CharField(min_length=4, label='Логин', max_length=45)
    password = forms.CharField(min_length=3, widget=forms.PasswordInput, label='Пароль', max_length=45)

    def __init__(self, *args, **kwargs):
        super(UserAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Логин'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Пароль'})


class AddTransactionForm(forms.ModelForm):
    class Meta:
        model = TransactionsModel
        fields = ['accountId_to', 'accountId_from', 'money', 'currency', 'comments', 'time_t']

    # accountId_to = forms.ModelChoiceField(label='accountId_to', queryset='')
    # accountId_from = forms.ModelChoiceField(label='accountId_from', queryset='')

    money = forms.IntegerField(label='money')
    currency = forms.CharField(max_length=10, label='currency')
    comments = forms.CharField(max_length=100, label='comment', empty_value=True)
    time_t = forms.DateTimeField(label='date', input_formats='%d/%m/%Y %H:%M', )



