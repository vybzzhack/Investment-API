# accounts/admin.py

from django.contrib import admin
from .models import InvestmentAccount, UserInvestmentAccount, Transaction

# Registering the InvestmentAccount model
@admin.register(InvestmentAccount)
class InvestmentAccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']

# Registering the UserInvestmentAccount model
@admin.register(UserInvestmentAccount)
class UserInvestmentAccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'account', 'permission']
    list_filter = ['permission']
    search_fields = ['user__username', 'account__name']

# Registering the Transaction model
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'user', 'amount', 'date']
    list_filter = ['account', 'user', 'date']
    search_fields = ['account__name', 'user__username']
