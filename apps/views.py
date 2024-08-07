from datetime import datetime
from decimal import Decimal

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import Currency, ExchangeRate


class CurrencyExchangeView(APIView):
    def get(self, request):
        base_currency_code = request.query_params.get('base_currency_code').upper()
        target_currency_code = request.query_params.get('target_currency_code').upper()
        convert_value = request.query_params.get('convert_value')

        rate = get_exchange_rate(base_currency_code, target_currency_code)
        if rate is not None:
            return Response(
                {'base_currency': base_currency_code, 'target_currency': target_currency_code,
                 'value': str(rate * Decimal(convert_value))},
                status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Exchange rate not found'}, status=status.HTTP_404_NOT_FOUND)


def get_exchange_rate(base_currency_code, target_currency_code):
    try:
        base_currency = Currency.objects.get(code=base_currency_code)
        target_currency = Currency.objects.get(code=target_currency_code)
    except Currency.DoesNotExist:
        return None

    if base_currency_code == target_currency_code:
        return Decimal('1.0')

    try:
        exchange_rate = ExchangeRate.objects.get(base_currency=base_currency, target_currency=target_currency)
        return exchange_rate.rate
    except ExchangeRate.DoesNotExist:
        return None


class CurrencyValueListView(APIView):
    def get(self, request):
        base_currency_code = request.query_params.get('base_currency').upper()
        if not base_currency_code:
            return Response({'error': 'Base currency code is required'}, status=400)

        data = get_currencies_with_base_value(base_currency_code)
        if data is not None:
            return Response({'status': status.HTTP_200_OK, 'date': datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                             'base_currency': base_currency_code,
                             'data': data})
        else:
            return Response({'error': 'Base currency not found'}, status=404)


def get_currencies_with_base_value(base_currency_code):
    try:
        base_currency = Currency.objects.get(code=base_currency_code)
    except Currency.DoesNotExist:
        return None

    currencies = Currency.objects.exclude(code=base_currency_code)
    result = []

    for currency in currencies:
        try:
            rate = ExchangeRate.objects.get(base_currency=base_currency, target_currency=currency).rate
        except ExchangeRate.DoesNotExist:
            try:
                inverse_rate = ExchangeRate.objects.get(base_currency=currency, target_currency=base_currency).rate
                rate = inverse_rate
            except ExchangeRate.DoesNotExist:
                rate = None

        if rate is not None:
            result.append({
                'currency_code': currency.code,
                'currency_name': currency.name,
                'value': str(rate)
            })

    return result
