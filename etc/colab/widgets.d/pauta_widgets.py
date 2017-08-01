from colab.widgets.widget_manager import WidgetManager
from colab_pauta.widgets.home_section import PautaHomeSectionWidget


WidgetManager.register_widget('home_section', PautaHomeSectionWidget())
