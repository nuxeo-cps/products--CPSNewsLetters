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
from Products.CMFCore.permissions import View, ModifyPortalContent

from Products.DCWorkflow.Transitions import TRIGGER_USER_ACTION

from Products.CPSWorkflow.transitions import \
     TRANSITION_INITIAL_PUBLISHING, TRANSITION_INITIAL_CREATE, \
     TRANSITION_ALLOWSUB_CREATE, TRANSITION_ALLOWSUB_PUBLISHING, \
     TRANSITION_BEHAVIOR_PUBLISHING, TRANSITION_BEHAVIOR_FREEZE, \
     TRANSITION_BEHAVIOR_DELETE, TRANSITION_BEHAVIOR_MERGE, \
     TRANSITION_ALLOWSUB_CHECKOUT, TRANSITION_INITIAL_CHECKOUT, \
     TRANSITION_BEHAVIOR_CHECKOUT, TRANSITION_ALLOW_CHECKIN, \
     TRANSITION_BEHAVIOR_CHECKIN, TRANSITION_ALLOWSUB_DELETE, \
     TRANSITION_ALLOWSUB_MOVE, TRANSITION_ALLOWSUB_COPY

from Products.CPSInstaller.CPSInstaller import CPSInstaller

WebDavLockItem = 'WebDAV Lock items'
WebDavUnlockItem = 'WebDAV Unlock items'

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
        wfdef = {'wfid': 'newsletter_wf',
                 'permissions': (View, ModifyPortalContent,
                                 WebDavLockItem, WebDavUnlockItem,),
                 'state_var': 'review_state',
                 }

        wfstates = {
            'pending': {
                'title': 'Waiting for reviewer',
                'transitions':('accept', 'reject'),
                 'permissions': {View: ('SectionReviewer', 'SectionManager',
                                        'Manager'),
                                 ModifyPortalContent: ('SectionReviewer',
                                        'SectionManager', 'Manager'),
                                 WebDavLockItem: ('SectionReviewer',
                                        'SectionManager', 'Manager'),
                                 WebDavUnlockItem: ('SectionReviewer',
                                        'SectionManager', 'Manager')},
            },
            'published': {
                'title': 'Public',
                'transitions': ('unpublish', 'cut_copy_paste',
                                'sub_publishing', 'newsletter_sendmail',),
                'permissions': {View: ('SectionReader', 'SectionReviewer',
                                       'SectionManager', 'Manager'),
                                ModifyPortalContent: ('Manager',),
                                WebDavLockItem: ('Manager',),
                                WebDavUnlockItem: ('Manager',)},
            },
        }

        wftransitions = {
            'publish': {
                'title': 'Member publishes directly',
                'new_state_id': 'published',
                'transition_behavior': (TRANSITION_INITIAL_PUBLISHING,
                                        TRANSITION_BEHAVIOR_FREEZE,
                                        TRANSITION_BEHAVIOR_MERGE),
                'clone_allowed_transitions': None,
                'after_script_name': '',
                'props': {'guard_permissions': '',
                          'guard_roles': 'Manager; SectionManager; '
                                         'SectionReviewer',
                          'guard_expr': ''},
            },
            'cut_copy_paste': {
                'title': 'Cut/Copy/Paste',
                'new_state_id': '',
                'transition_behavior': (TRANSITION_ALLOWSUB_DELETE,
                                        TRANSITION_ALLOWSUB_MOVE,
                                        TRANSITION_ALLOWSUB_COPY),
                'clone_allowed_transitions': None,
                'trigger_type': TRIGGER_USER_ACTION,
                'actbox_name': '',
                'actbox_category': '',
                'actbox_url': '',
                'props': {'guard_permissions': '',
                          'guard_roles': 'Manager; SectionManager; '
                                        'SectionReviewer',
                          'guard_expr': ''},
            },
            'submit': {
                'title': 'Member requests publishing',
                'new_state_id': 'pending',
                'transition_behavior': (TRANSITION_INITIAL_PUBLISHING,
                                        TRANSITION_BEHAVIOR_FREEZE),
                'clone_allowed_transitions': None,
                'after_script_name': '',
                'actbox_name': '',
                'actbox_category': '',
                'actbox_url': '',
                'props': {'guard_permissions': '',
                          'guard_roles': 'Manager; Member',
                          'guard_expr': ''},
            },
            'accept': {
                'title': 'Reviewer accepts publishing',
                'new_state_id': 'published',
                'transition_behavior': (TRANSITION_BEHAVIOR_MERGE,),
                'clone_allowed_transitions': None,
                'after_script_name': '',
                'trigger_type': TRIGGER_USER_ACTION,
                'actbox_name': 'action_accept',
                'actbox_category': 'workflow',
                'actbox_url': '%(content_url)s/content_accept_form',
                'props': {'guard_permissions': '',
                          'guard_roles': 'Manager; SectionManager; '
                                         'SectionReviewer',
                          'guard_expr': ''},
            },
            'reject': {
                'title': 'Reviewer rejects publishing',
                'new_state_id': '',
                'transition_behavior': (TRANSITION_BEHAVIOR_DELETE,),
                'clone_allowed_transitions': None,
                'trigger_type': TRIGGER_USER_ACTION,
                'actbox_name': 'action_reject',
                'actbox_category': 'workflow',
                'actbox_url': '%(content_url)s/content_reject_form',
                'props': {'guard_permissions': '',
                          'guard_roles': 'Manager; SectionManager; '
                                         'SectionReviewer',
                          'guard_expr': ''},
            },
            'unpublish': {
                'title': 'Reviewer removes content from publication',
                'new_state_id': '',
                'transition_behavior': (TRANSITION_BEHAVIOR_DELETE,),
                'clone_allowed_transitions': None,
                'trigger_type': TRIGGER_USER_ACTION,
                'actbox_name': 'action_un_publish',
                'actbox_category': 'workflow',
                'actbox_url': '%(content_url)s/content_unpublish_form',
                'props': {'guard_permissions': '',
                          'guard_roles': 'Manager; SectionManager; '
                                         'SectionReviewer',
                          'guard_expr': ''},
            },
            'sub_publishing': {
                'title': 'Allow publishing of subdocuments',
                'new_state_id': '',
                'transition_behavior': (TRANSITION_ALLOWSUB_PUBLISHING,),
                'clone_allowed_transitions': None,
                'trigger_type': TRIGGER_USER_ACTION,
                'props': {'guard_permissions': '',
                          'guard_roles': 'Manager; SectionManager; '
                                         'SectionReviewer; SectionReader',
                          'guard_expr': ''},
            },
            'newsletter_sendmail' : {
                'title':'Silent transition',
                'description':'',
                'new_state_id':'',
                'transition_behavior':(),
                'clone_allowed_transitions':None,
                'trigger_type':TRIGGER_USER_ACTION,
                'actbox_name':'action_news_letter_sendmail',
                'actbox_category':'workflow',
                'actbox_url':'%(content_url)s/newsletter_sendmail',
                'props':{'guard_permissions': '',
                         'guard_roles': 'Manager; SectionManager; \
                         SectionReviewer; Owner',
                         'guard_expr': ''},
            },
        }

        wfscripts = {
        }

        wfvariables = {
            'action': {
                'description': 'The last transition',
                'default_expr': 'transition/getId|nothing',
                'for_status': 1,
                'update_always': 1,
            },
            'actor': {
                'description': 'The ID of the user who performed',
                'default_expr': 'user/getId',
                'for_status': 1,
                'update_always': 1,
            },
            'comments': {
                'description': 'Comments about the last transition',
                'default_expr': "python:state_change.kwargs.get('comment', '')",
                'for_status': 1,
                'update_always': 1,
            },
            'review_history': {
                'description': 'Provides access to workflow history',
                'default_expr': 'state_change/getHistory',
                'props': {'guard_permissions': '',
                          'guard_roles': 'Manager; SectionManager; '
                                         'SectionReviewer',
                          'guard_expr': ''}
            },
            'language_revs': {
                'description': 'The language revisions of the proxy',
                'default_expr': 'state_change/getLanguageRevisions',
                'for_status': 1,
                'update_always': 1,
            },
            'time': {
                'description': 'Time of the last transition',
                'default_expr': 'state_change/getDateTime',
                'for_status': 1,
                'update_always': 1,
                'for_catalog': 1,
            },
            'dest_container': {
                'description': 'Destination container for the last '
                                'paste/publish',
                'default_expr': "python:state_change.kwargs.get("
                                "'dest_container', '')",
                'for_status': 1,
                'update_always': 1,
            },
        }
        self.verifyWorkflow(wfdef, wfstates, wftransitions,
                     wfscripts, wfvariables)

    #def installNewsLetterWorkflow(self):
    #    """Install the newsletter section workflow type
    #    """
    #
    #    from Products.CPSNewsLetters.Workflows.NewsLetterWorkflow import \
    #         newsletterWorkflowInstall
    #    newsletterWorkflowInstall(self.portal.this())

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
