##parameters=
#$Id$
"""Return newsletter related types.
"""

#################################################
#################################################

newsletter_type = {
    'title': 'portal_type_CPS_News_Letter_title',
    'description': 'portal_type_CPS_News_Letter_description',
    'content_icon': 'newsletterdocument_icon.gif',
    'content_meta_type': 'CPS Document',
    'product': 'CPSDocument',
    'factory': 'addCPSDocument',
    'immediate_view': 'cpsdocument_view',
    'global_allow': True,
    'filter_content_types': True,
    'allowed_content_types': (),
    'allow_discussion': False,
    'cps_is_searchable': True,
    'cps_proxy_type': 'document',
    'cps_display_as_document_in_listing': True,
    'schemas': ('metadata', 'common', 'newsletter'),
    'layouts': ('common', 'newsletter'),
    'flexible_layouts': (),
    'storage_methods': (),
    'actions': (
         {'id': 'view',
          'name': 'action_view',
          'action': 'string:${object_url}/cpsdocument_view',
          'condition': '',
          'permission': ('View',),
          'category': 'object',
          'visible': 1,},
         {'id': 'new_content',
          'name': 'action_new_content',
          'action': 'string:${object_url}/folder_factories',
          'condition': "python:object.getTypeInfo().cps_proxy_type != 'document'",
          'permission': ('Modify portal content',),
          'category': 'object',
          'visible': 1,},
         {'id': 'contents',
          'name': 'action_folder_contents',
          'action': 'string:${object_url}/folder_contents',
          'condition': "python:object.getTypeInfo().cps_proxy_type != 'document'",
          'permission': ('Modify portal content',),
          'category': 'object',
          'visible': 1,},
         {'id': 'edit',
          'name': 'action_edit',
          'action': 'string:${object_url}/cpsdocument_edit_form',
          'condition': '',
          'permission': ('Modify portal content',),
          'category': 'object',
          'visible': 1,},
         {'id': 'metadata',
          'name': 'action_metadata',
          'action': 'string:${object_url}/cpsdocument_metadata',
          'condition': '',
          'permission': ('View',),
          'category': 'object',
          'visible': 1,},
         {'id': 'localroles',
          'name': 'action_local_roles',
          'action': 'string:${object_url}/folder_localrole_form',
          'condition': "python:object.getTypeInfo().cps_proxy_type != 'document'",
          'permission': ('Change permissions',),
          'category': 'object',
          'visible': 1,},
    )
}

#################################################
#################################################

types = {}
types['NewsLetter'] = newsletter_type

#################################################
#################################################

return types
