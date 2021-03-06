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

""" CPS NewsLetters component

This component provides NewsLetters content type and register itself
within the portal_subscriptions tool if CPSSubscriptions is installed.
"""

from Products.CMFCore.DirectoryView import registerDirectory
from Products.GenericSetup import profile_registry
from Products.GenericSetup import EXTENSION

from Products.CPSCore.interfaces import ICPSSite

profile_registry.registerProfile(
        'default',
        'CPS NewsLetters',
        "NewsLetters product for CPS.",
        'profiles/default',
        'CPSNewsLetters',
         EXTENSION,
         for_=ICPSSite)
registerDirectory('skins', globals())
