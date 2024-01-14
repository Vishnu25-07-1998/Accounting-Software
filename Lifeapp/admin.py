from django.contrib import admin
from . models import FinancialRecord, BankStatement


# Register your models here.
admin.site.register(FinancialRecord)
admin.site.register(BankStatement)
