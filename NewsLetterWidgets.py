# -*- coding: ISO-8859-15 -*-
# Copyright (c) 2004 Nuxeo SARL <http://nuxeo.com>
# Author : Julien Anguenot <ja@nuxeo.com>

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
# $Id$

__author__ = "Julien Anguenot <mailto:ja@nuxeo.com>"

""" CPS NewsLetters Widgets

Containers newsletter spcicific widgets. It has to cope with the fact that the
render of the newsletter might arrive within the mail client.
"""

from Globals import InitializeClass

from Products.CPSSchemas.WidgetTypesTool import WidgetTypeRegistry
from Products.CPSSchemas.BasicWidgets import CPSWidgetType
from Products.CPSSchemas.ExtendedWidgets import CPSInternalLinksWidget

class CPSNewsLetterInternalLinksWidget(CPSInternalLinksWidget):
    """CPS Newsletter InternalLinks Widget.

    We need absolute urls since it will be displayed within a mail client if
    the newsletter is going to be rendered within the notification email.
    """

    meta_type = "CPS NewsLetter InternalLinks Widget"

    def render(self, mode, datastructure, **kw):
        """Render in mode from datastructure."""
        if mode not in ('view', 'edit'):
            raise RuntimeError('unknown mode %s' % mode)

        render_method = 'widget_newsletter_internallinks_render'
        meth = getattr(self, render_method, None)

        return meth(mode=mode, datastructure=datastructure)

InitializeClass(CPSNewsLetterInternalLinksWidget)

class CPSNewsLetterInternalLinksWidgetType(CPSWidgetType):
    """CPS NewsLetter InternalLinks Widget Type
    """

    meta_type = "CPS NewsLetter InternalLinks Widget Type"
    cls = CPSNewsLetterInternalLinksWidget

InitializeClass(CPSNewsLetterInternalLinksWidgetType)

##################################################################
#   Register widget types
##################################################################

WidgetTypeRegistry.register(CPSNewsLetterInternalLinksWidgetType)
