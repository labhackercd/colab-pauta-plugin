name = 'colab_pauta'
verbose_name = 'Colab Pauta Participativa Plugin'

upstream = 'http://127.0.0.1:6000/'
api_key = 'api_key'

urls = {
    'include': 'colab_pauta.urls',
    'prefix': '^pauta/',
}
