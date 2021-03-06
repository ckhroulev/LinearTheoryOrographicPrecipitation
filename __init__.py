# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LinearTheoryOrographicPrecipitation
                                 A QGIS plugin
 Implements the Smith & Barstad (2004) LT model
                             -------------------
        begin                : 2016-09-15
        copyright            : (C) 2016 by Andy Aschwanden
        email                : andy.aschwanden@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

import os
import qgis.utils

# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LinearTheoryOrographicPrecipitation class from file LinearTheoryOrographicPrecipitation.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    plugin_name = os.path.dirname(__file__).split(os.path.sep)[-1]
    plugin_name = qgis.utils.pluginMetadata(plugin_name, 'name')
    try:
        # qgis.PyQt is available in QGIS >=2.14
        from qgis.PyQt.QtCore import qVersion
        # qgis.utils.QGis is available in QGIS < 3
        if hasattr(qgis.utils, 'QGis'):
            import qgis2compat.apicompat
            qgis2compat.log('apicompat used in %s' % plugin_name)
    except ImportError:
        try:
            # we are in QGIS < 2.14
            import qgis2compat
            import qgis2compat.apicompat
            qgis2compat.log('PyQt and apicompat used in %s' % plugin_name)
        except ImportError:
            import traceback
            message = ('The Plugin %s uses the QGIS2compat plugin. '
                       'Please install it with the plugin manager it and '
                       'restart QGIS. For more information read '
                       'http://opengis.ch/qgis2compat' %
                       plugin_name)
            traceback.print_exc()
            raise ImportError(message)

    from .lt_model import LinearTheoryOrographicPrecipitation
    return LinearTheoryOrographicPrecipitation(iface)
