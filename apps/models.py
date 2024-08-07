from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)  # ISO 4217 currency code (e.g., USD, EUR)
    name = models.CharField(max_length=50, blank=True)  # Full name of the currency (e.g., US Dollar, Euro)
    symbol = models.CharField(max_length=10, blank=True)  # Symbol used for the currency (e.g., $, €)

    def __str__(self):
        return f"{self.name} ({self.code})"


class ExchangeRate(models.Model):
    base_currency = models.ForeignKey(Currency, related_name='base_rates', on_delete=models.CASCADE)
    target_currency = models.ForeignKey(Currency, related_name='target_rates', on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=10, decimal_places=4)  # Exchange rate from base to target currency

    class Meta:
        unique_together = ('base_currency', 'target_currency')

    def __str__(self):
        return f"1 {self.base_currency.code} = {self.rate} {self.target_currency.code}"
