from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.db import models


# Create your views here.
from lab5.polls.models import BankModel


class Base(View):
    def get(self, request):
        return render(request, 'Base.html')


class Home(View):
    def get(self, request):
        return render(request, 'home.html')


class Bank(View):
    def get(self, request):
        data_banks = {
            'banks': [
                {'title': 'Альфа', 'id': 1},
                {'title': 'Сбер', 'id': 2},
                {'title': 'Северный кредит', 'id': 3},
                {'title': 'БКС', 'id': 4}
            ]
        }
        return render(request, 'Bank.html', data_banks)


class BankView1(View):
    def get(self, request, id):
        data = {'bank': {'id': id}}
        return render(request, 'Bank_view.html', data)


class Trans(View):
    def get(self, request):
        transactions = {'trans': 'Пользователь - транзакция - банк'}
        return render(request, 'Trans.html', transactions)


        #########################
        #         lab6          #
        #########################

class BankView(View):
    def get(self, request, id):
        data = BankModel.objects.all()
        return render(request, 'Bank_view.html', {''})