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

"""NewsLetter type workflow definition

The idea in here is to have one more transition for being able to send an event
to the event_service tool and then taking actions through CPSSubscriptions
"""

import os, sys

from Products.DCWorkflow.Transitions import \
     TRIGGER_USER_ACTION

def newsletterWorkflowInstall(self):
    """Installs the workflow for the NewsLetter Type
    """

    portal = self.portal_url.getPortalObject()
    wftool = portal.portal_workflow

    wfids = wftool.objectIds()
    wfid = 'newsletter_wf'

    if wfid in wfids:
        wftool.manage_delObjects([wfid])

    wftool.manage_addWorkflow(id=wfid,
                              workflow_type='cps_workflow (Web-configurable workflow for CPS)')

    wf = wftool[wfid]

    wf_ref_id = 'section_content_wf'
    wf_ref = wftool[wf_ref_id]

    #
    # Permissions
    # We keep the same as the ref workflow
    #

    wf.permissions = wf_ref.permissions

    #
    # States
    # We add the newsletter_sendmail transition as possible transition
    # within the published state
    #

    wf.states = wf_ref.states
    s = wf.states.get('published')
    s.transitions = s.transitions + ('newsletter_sendmail',)

    #
    # Transitions
    # We add one silent transition representing the mail sending
    #

    wf.transitions = wf_ref.transitions

    new_transition_id = 'newsletter_sendmail'
    if wf_ref.transitions.get(new_transition_id) is None:
        wf.transitions.addTransition(new_transition_id)

    t = wf.transitions.get('newsletter_sendmail')
    t.setProperties(title='Silent transition',
                    description='',
                    new_state_id='',
                    transition_behavior=(),
                    clone_allowed_transitions=None,
                    trigger_type=TRIGGER_USER_ACTION,
                    actbox_name='action_news_letter_sendmail',
                    actbox_category='workflow',
                    actbox_url='%(content_url)s/newsletter_sendmail',
                    props={'guard_permissions':'',
                           'guard_roles':'Manager; SectionManager; \
                           SectionReviewer; Owner',
                           'guard_expr':''},)

    #
    # Variables
    # We keep the same as the ref workflow
    #

    wf.variables = wf_ref.variables
    wf.state_var = wf_ref.state_var

    #
    # Scripts
    # No additional scripts
    #

    wf.scripts = wf_ref.scripts
