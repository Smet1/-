"""lab6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from myapp.views import Bank, BankInDetail, Customer, CustomerInDetail, Home, CustomerAccounts, CustomerTransactions,\
    reg_view, auth_view, logout_view, registration1, add_transaction

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', Home.as_view(), name='home'),

    url(r'^bank/$', Bank.as_view(), name='banks_main'),
    url(r'^bank/(?P<id>\d+)/$', BankInDetail.as_view(), name='banks_detail'),
    url(r'^customers/$', Customer.as_view(), name='customers_main'),
    url(r'^customers/(?P<id>\d+)/$', CustomerInDetail.as_view(), name='customers_detail'),
    url(r'^accounts/$', CustomerAccounts.as_view(), name='accts'),
    url(r'^transactions/$', CustomerTransactions.as_view(), name='trans'),
    url(r'^reg/$', reg_view, name='reg'),
    url(r'^auth/$', auth_view, name='auth'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^add/$', add_transaction, name='add_trans')
]
