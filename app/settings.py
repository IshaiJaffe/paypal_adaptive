# settings for app

PAYPAL_ENDPOINT = 'https://svcs.sandbox.paypal.com/AdaptivePayments/' # sandbox
#PAYPAL_ENDPOINT = 'https://svcs.paypal.com/AdaptivePayments/' # production

PAYPAL_PAYMENT_HOST = 'https://www.sandbox.paypal.com/au/cgi-bin/webscr' # sandbox
#PAYPAL_PAYMENT_HOST = 'https://www.paypal.com/webscr' # production

PAYPAL_USERID = 'ishai_1303985950_biz_api1.empeeric.com'
PAYPAL_PASSWORD = '1303985963'
PAYPAL_SIGNATURE = 'ALLH9tNIUt-i8AP6XpP5O2QPfdoHAq1JGxilnOUmW86N6wtJFnT1ASUZ'
PAYPAL_APPLICATION_ID = 'APP-80W284485P519543T' # sandbox only
PAYPAL_EMAIL = 'ishai_1303985950_biz@empeeric.com'

PAYPAL_COMMISSION = 0.2 # 20%

USE_CHAIN = True
USE_IPN = False
USE_EMBEDDED = False
SHIPPING = False # not yet working properly; PayPal bug
IS_DELAYED = True

# EMBEDDED_ENDPOINT = 'https://paypal.com/webapps/adaptivepayment/flow/pay'
EMBEDDED_ENDPOINT = 'https://www.sandbox.paypal.com/webapps/adaptivepayment/flow/pay'
