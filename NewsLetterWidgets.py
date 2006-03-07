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
# $Id: __init__.py 31654 2006-01-16 00:48:47Z fguillaume $

from Products.CPSSchemas.ExtendedWidgets import CPSInternalLinksWidget as \
     CPSNewsLetterInternalLinksWidget
from warnings import warn

warn("The widget CPSNewsLetterInternalLinksWidget, is a deprecated "
     "compatiblity alias for CPSInternalLinksWidget. "
     "Please use that widget instead. "
     "CPSNewsLetterInternalLinksWidget will be removed in CPS 3.5.",
     DeprecationWarning)
