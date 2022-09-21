from django.contrib import admin


from api.models import Account, User, Stock, Investment, UserHolding


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass

@admin.register(Investment)
class StockAdmin(admin.ModelAdmin):
    pass

@admin.register(UserHolding)
class StockAdmin(admin.ModelAdmin):
    pass


