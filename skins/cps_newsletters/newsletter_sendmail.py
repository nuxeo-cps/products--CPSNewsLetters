##parameters=REQUEST=None
"""Follow the transition to send an event_id to the event_service tool
"""

wftool = context.portal_workflow
wftool.doActionFor(context, 'newsletter_sendmail')

if REQUEST is not None:
    psm= "psm_newsletter_successfully_sent"
    url = context.absolute_url() + \
          '?portal_status_message=' + \
          psm
    REQUEST.RESPONSE.redirect(url)
