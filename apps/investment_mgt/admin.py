from django.contrib import admin

from apps.investment_mgt.models import User, Account, Investment, Stock, UserHolding


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    pass

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass

@admin.register(UserHolding)
class UserHoldingAdmin(admin.ModelAdmin):
    pass


