from django.shortcuts import render
from django.views import View
from myapp.models import BankModel
# Create your views here.


class Bank(View):
    def get(self, request):
        data = BankModel.objects.all()
        return render(request, 'banks_main.html', {'banks': data})


class BankInDetail(View):
    def get(self, request, id):
        data = BankModel.objects.get(idBanks=int(id))
        data_out = {
            'banks':{
                'id': id,
                'name': data.name,
                'address': data.address
            }
        }
        return render(request, 'bank_detail.html', {'banks': data})
