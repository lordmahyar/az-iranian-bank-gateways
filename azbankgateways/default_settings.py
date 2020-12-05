"""Default settings for messaging."""

from django.conf import settings

_AZ_IRANIAN_BANK_GATEWAYS = getattr(settings, 'AZ_IRANIAN_BANK_GATEWAYS', {})
BANK_CHANNELS = _AZ_IRANIAN_BANK_GATEWAYS.get('CHANNELS', {})
BANK_DEFAULT = _AZ_IRANIAN_BANK_GATEWAYS.get('DEFAULT', 'BMI')
CURRENCY = _AZ_IRANIAN_BANK_GATEWAYS.get('CURRENCY', 'IRR')
CALLBACK_URL = _AZ_IRANIAN_BANK_GATEWAYS.get('CALLBACK_URL', '/bankgateways/callback')
TRANSACTION_QUERY_PARAM = _AZ_IRANIAN_BANK_GATEWAYS.get('TRANSACTION_QUERY_PARAM', 'tc')
