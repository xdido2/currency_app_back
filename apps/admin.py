from django.contrib import admin

from apps.models import Currency, ExchangeRate

admin.site.register(Currency)
admin.site.register(ExchangeRate)
