##parameters=
#$Id$
"""Return the newsletters related schemas
"""

True  = 1
False = 0

#################################################
#################################################

newsletter_schema = {
    'mailBodyFooter': {
        'type': 'CPS String Field',
        'data': {
            'default_expr': 'string:',
            'is_searchabletext': False,
            'acl_read_permissions': '',
            'acl_read_roles': '',
            'acl_read_expr': '',
            'acl_write_permissions': '',
            'acl_write_roles': '',
            'acl_write_expr': '',
            'read_ignore_storage': False,
            'read_process_expr': '',
            'read_process_dependent_fields': (),
            'write_ignore_storage': False,
            'write_process_expr': '',
        },
    },
    'mailBodyHeader': {
        'type': 'CPS String Field',
        'data': {
            'default_expr': 'string:',
            'is_searchabletext': False,
            'acl_read_permissions': '',
            'acl_read_roles': '',
            'acl_read_expr': '',
            'acl_write_permissions': '',
            'acl_write_roles': '',
            'acl_write_expr': '',
            'read_ignore_storage': False,
            'read_process_expr': '',
            'read_process_dependent_fields': (),
            'write_ignore_storage': False,
            'write_process_expr': '',
        },
    },
    'results': {
        'type': 'CPS String List Field',
        'data': {
            'default_expr': 'python:[]',
            'is_searchabletext': False,
            'acl_read_permissions': '',
            'acl_read_roles': '',
            'acl_read_expr': '',
            'acl_write_permissions': '',
            'acl_write_roles': '',
            'acl_write_expr': '',
            'read_ignore_storage': False,
            'read_process_expr': '',
            'read_process_dependent_fields': (),
            'write_ignore_storage': False,
            'write_process_expr': '',
        },
    },
}

###############################################
###############################################

schemas = {}
schemas['newsletter'] = newsletter_schema

###############################################
###############################################

return schemas
