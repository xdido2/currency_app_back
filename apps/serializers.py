from rest_framework.serializers import ModelSerializer

from apps.models import Currency


class CurrencySerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = ['name', 'value']
