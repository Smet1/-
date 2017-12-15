from django import forms
from .models import CustomerModel


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
