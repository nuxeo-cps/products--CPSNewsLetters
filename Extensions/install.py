# -*- coding: ISO-8859-15 -*-
# Copyright (c) 2004 Nuxeo SARL <http://nuxeo.com>
# Author: Julien Anguenot <ja@nuxeo.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
# 02111-1307, USA.
#
# $Id$

""" CPSNewsLetters Installer

Installer/Updater fot the CPSNewsLetters component.
"""

from zLOG import LOG, INFO, DEBUG

from Products.CMFCore.utils import getToolByName
from Products.CPSInstaller.CPSInstaller import CPSInstaller

SECTIONS_ID = 'sections'
WORKSPACES_ID = 'workspaces'
SKINS = {
    'cps_newsletters' :
    'Products/CPSNewsLetters/skins/cps_newsletters',
    }

class CPSNewsLettersInstaller(CPSInstaller):
    """ Installer class for CPS NewsLetters component

    Intended to be use as an Installer/Updater tool.
    """

    product_name = 'CPSNewsLetters'

    def install(self):
        """ Installs the compulsory elements.

        Calling feature methods.
        """

        self.log("Install/Update : CPSNewsLetters Product")
        self.verifySkins(SKINS)
        self.resetSkinCache()
        self.setupTranslations()
        self.installSchemas()
        self.verifyWidgets(self.portal.getCPSNewsLettersDocumentWidgets())
        self.installLayouts()
        self.installTypes()
        self.installNewsLetterWorkflow()
        self.updateWorkflowAssociations()
        self.setupSubscriptionsTool()
        self.finalize()
        self.log("End of Install/Update : CPSNewsLetters Product")

    def installSchemas(self):
        """Install the newsletters related schemas
        """

        self.log("  Verifiying newsletters related schemas ")

        stool = self.portal.portal_schemas

        schemas = self.portal.getCPSNewsLettersDocumentSchemas()

        for id, info in schemas.items():
            self.log(" Schema %s" % id)
            if id in stool.objectIds():
                self.log("  Deleting.")
                stool.manage_delObjects([id])
            self.log("  Installing.")
            schema = stool.manage_addCPSSchema(id)
            for field_id, fieldinfo in info.items():
                self.log("   Field %s." % field_id)
                schema.manage_addField(field_id, fieldinfo['type'],
                                       **fieldinfo['data'])

    def installLayouts(self):
        """Install the newsletters related layouts
        """

        self.log("Verifiying layouts")

        ltool = self.portal.portal_layouts

        layouts = self.portal.getCPSNewsLettersDocumentLayouts()

        for id, info in layouts.items():
            self.log(" Layout %s" % id)
            if id in ltool.objectIds():
                self.log("  Deleting.")
                ltool.manage_delObjects([id])
            self.log("  Installing.")
            layout = ltool.manage_addCPSLayout(id)
            for widget_id, widgetinfo in info['widgets'].items():
                self.log("   Widget %s" % widget_id)
                widget = layout.manage_addCPSWidget(widget_id, widgetinfo['type'],
                                                    **widgetinfo['data'])
                layout.setLayoutDefinition(info['layout'])
                layout.manage_changeProperties(**info['layout'])


    def installTypes(self):
        """Install the newsletters related types
        """

        self.log("Verifying portal types")

        self.ttool = self.portal.portal_types

        self.flextypes = self.portal.getCPSNewsLettersDocumentTypes()
        self.newptypes = self.flextypes.keys()
        self.verifyFlexibleTypes(self.flextypes)
        types = self.newptypes
        self.allowContentTypes(types, 'Workspace')

    def installNewsLetterWorkflow(self):
        """Install the newsletter section workflow type
        """

        from Products.CPSNewsLetters.Workflows.NewsLetterWorkflow import \
             newsletterWorkflowInstall
        newsletterWorkflowInstall(self.context)

    def updateWorkflowAssociations(self):
        """Update workflow associations for newsletter types
        """

        ws_chain = {}
        se_chain = {}

        for ptype in self.newptypes:
            ws_chain[ptype] = 'workspace_content_wf'
            se_chain[ptype] = 'newsletter_wf'

        for ptype in self.newptypes:
            wf = self.flextypes[ptype].get('cps_workspace_wf',
                                           'workspace_content_wf')
            ws_chain[ptype] = wf
            wf = self.flextypes[ptype].get('cps_section_wf',
                                           'newsletter_wf')
            se_chain[ptype] = wf

        self.verifyLocalWorkflowChains(self.portal[WORKSPACES_ID], ws_chain)
        self.verifyLocalWorkflowChains(self.portal[SECTIONS_ID], se_chain)

    def setupSubscriptionsTool(self):
        """Setup subscriptions tool

        Registering on more event related to newsletters.
        """

        subtool = getToolByName(self.portal, 'portal_subscriptions', None)

        if subtool is not None:
            subtool.manage_addEventType('Section',
                                        'workflow_newsletter_sendmail',
                                        'label_newsletter_sendmail')
            subtool.addRenderedEvent('workflow_newsletter_sendmail')
        else:
            LOG(":: CPSNewsLetters ::", DEBUG,
                "CPSSubscriptions is not installed.",
                "You may install it if you want use the subscriptions \
                facilities it provides with CPSNewsLetters")


###############################################
# __call__
###############################################

def install(self):
    """Installation is done here.

    Called by an external method for instance.
    """
    installer = CPSNewsLettersInstaller(self)
    installer.install()
    return installer.logResult()
