
from colab.plugins.data import PluginDataImporter


class ColabPautaDataImporter(PluginDataImporter):
    app_label = 'colab_pauta'

    def fetch_data(self):
        pass
