"""
Local variables that can be used all across the application.

Some may be used in other python modules, and they can also
be imported into templates.

"""

COMPANY_NAME = 'Hazel\'s Dessert Shoppe'
COMPANY_ADDRESS1 = '2715 Raven Falls Lane'
COMPANY_ADDRESS2 = None
COMPANY_CITY = 'Friendswood'
COMPANY_STATE = 'Texas'
COMPANY_POSTAL_CODE = '77546'
COMPANY_COUNTRY = 'United States'

SITE_NAME = 'Inc.'
FULL_SITE_NAME = '{} {}'.format(COMPANY_NAME, SITE_NAME)

CONFIG_CONTEXT = {
    'company_name': COMPANY_NAME,
    'site_name': SITE_NAME,
    'full_site_name': FULL_SITE_NAME,
    'company_address1': COMPANY_ADDRESS1,
    'company_address2': COMPANY_ADDRESS2,
    'company_city': COMPANY_CITY,
    'company_state': COMPANY_STATE,
    'company_postal_code': COMPANY_POSTAL_CODE,
    'company_country': COMPANY_COUNTRY
}
