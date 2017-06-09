import os.path as path

img_prefix = path.abspath(path.join(path.dirname(path.abspath(__file__)), "resources", "img"))
if not path.exists(img_prefix):
    img_prefix = path.abspath(path.join(path.dirname(path.abspath(__file__)), "..", "..", "resources", "img"))

text_prefix = path.abspath(path.join(path.dirname(path.abspath(__file__)), "resources", "text"))
if not path.exists(text_prefix):
    text_prefix = path.abspath(path.join(path.dirname(path.abspath(__file__)), "..", "..", "resources", "text"))


def resource_icon_path(name):
    return path.join(img_prefix, name)


def resource_icon(name):
    """Load an image as an icon"""
    from PyQt4.QtGui import QIcon
    return QIcon(resource_icon_path(name))


def resource_text_path(name):
    return path.join(text_prefix, name)


def resource_text(name):
    with open(resource_text_path(name)) as text:
        return text.read()


from .arrayspinbox import ArraySpinBox
from ._indexcontroller import IndexController
from ._samplescalecontroller import SampleScaleController
from ._plotexportsettingscontroller import PlotExportSettingsWidget

from .colormapcombo import ColormapCombo
from .layoutcombo import LayoutCombo
from .layoutfigure import LayoutFigure
from .layoutcanvas import LayoutCanvas

from .slicemodel import SliceModel, SliceDirection
from .slicedatasource import SliceDataSource
from .sliceviewcontext import SliceViewContext
from .sliceview import SliceView
from .sliceviewwidget import SliceViewWidget
from .settingswindow import SettingsWindow
from .segyviewwidget import SegyViewWidget

__version__ = '1.0.7'
__copyright__ = 'Copyright 2016, Statoil ASA'
__license__ = 'GNU Lesser General Public License version 3'
__status__ = 'Production'
