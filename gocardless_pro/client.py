# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import services
from .http_client import HttpClient

class Client(object):
    """Client for interacting with the GoCardless Pro API.

    Instantiate a client object with your access token and environment, then
    use the resource methods to access the API.

    Args:
      access_token (str): Find or generate this in your GoCardless Pro dashboard
        (https://manage.gocardless.com/organisation/access-tokens).
      environment (str): Either 'sandbox' or 'live'.
      base_url (str): Manually set a base URL. Most people should use
        `environment` instead.

    Example:
      client = Client(access_token=ACCESS_TOKEN, environment='sandbox')
      for customer in client.customers.list():
          print '{} {}'.format(customer.family_name, customer.given_name)
    """

    def __init__(self, access_token=None, environment=None, base_url=None):
        if access_token is None:
            raise ValueError('No access_token provided')

        if environment is None and base_url is None:
            raise ValueError('No environment or base_url specified')

        base_url = base_url or self._environment_url(environment)
        self._http_client = HttpClient(base_url, access_token)

    @property
    def creditors(self):
        return services.CreditorsService(self._http_client)

    @property
    def creditor_bank_accounts(self):
        return services.CreditorBankAccountsService(self._http_client)

    @property
    def customers(self):
        return services.CustomersService(self._http_client)

    @property
    def customer_bank_accounts(self):
        return services.CustomerBankAccountsService(self._http_client)

    @property
    def events(self):
        return services.EventsService(self._http_client)

    @property
    def helpers(self):
        return services.HelpersService(self._http_client)

    @property
    def mandates(self):
        return services.MandatesService(self._http_client)

    @property
    def modulus_checks(self):
        return services.ModulusChecksService(self._http_client)

    @property
    def payments(self):
        return services.PaymentsService(self._http_client)

    @property
    def payouts(self):
        return services.PayoutsService(self._http_client)

    @property
    def redirect_flows(self):
        return services.RedirectFlowsService(self._http_client)

    @property
    def refunds(self):
        return services.RefundsService(self._http_client)

    @property
    def subscriptions(self):
        return services.SubscriptionsService(self._http_client)

    def _environment_url(self, environment):
        environment_urls = { 
            'live': 'https://api.gocardless.com',
            'sandbox': 'https://api-sandbox.gocardless.com',
        }

        if environment not in environment_urls:
            msg = 'Invalid environment "{env}", use one of {env_names}'.format(
                env=environment,
                env_names=', '.join(environment_urls.keys())
            )
            raise ValueError(msg)

        return environment_urls[environment]
