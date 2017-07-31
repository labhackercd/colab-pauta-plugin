
from django.utils.translation import ugettext_lazy as _
from colab.plugins.utils.menu import colab_url_factory

name = 'colab_pauta'
verbose_name = 'Colab Pauta Plugin'

upstream = 'localhost'
# middlewares = []

urls = {
    'include': 'colab_pauta.urls',
    'prefix': '^colab_pauta/',
}

menu_title = _('colab_pauta')

url = colab_url_factory('colab_pauta')

# Extra data to be exposed to plugin app config
extra = {}

menu_urls = (
# Example of menu URL:
#    url(display=_('Public Projects'), viewname='colab_pauta',
#        kwargs={'path': 'public/projects'}, auth=False),

# Example of authenticated user menu URL:
#    url(display=_('Profile'), viewname='colab_pauta',
#        kwargs={'path': 'profile'}, auth=True),
)
