from django.urls import path 
from . import views
from .views import custom_login

urlpatterns = [
    path('index',views.index, name= 'index'),
    path('voucher', views.voucher, name='voucher'),
    path('Balancesheet', views.Account_Master, name = 'balancesheet'),
    path('finance', views.financebook, name = 'financebook'),
    path('bank', views.bank, name = 'bank'),
    path('reconcile', views.reconcile, name='reconcile'),
    path('base', views.base, name='base'),
    path('Ledger', views.ledger, name='ledger'),
    path('', custom_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
