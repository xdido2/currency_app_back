from django.urls import path

from apps.views import CurrencyExchangeView, CurrencyValueListView

urlpatterns = [
    path('exchange-rate/', CurrencyExchangeView.as_view(),
         name='currency-exchange-rate'),
    path('currencies/value/', CurrencyValueListView.as_view(), name='currency-value-list'),

]
