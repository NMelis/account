from django.contrib import admin

from server.apps.account.models import Account


@admin.register(Account)
class AdminAccount(admin.ModelAdmin):
    pass
