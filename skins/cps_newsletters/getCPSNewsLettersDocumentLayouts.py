##parameters=
#$Id$
"""Return the newsletters related layouts
"""

True  = 1
False = 0

newsletter_layout = {
    'widgets': {
        'mailBodyFooter': {
            'type': 'Text Widget',
            'data': {
                'fields': ['mailBodyFooter'],
                'is_i18n': 1,
                'label_edit': 'label_newsletter_mailbody_footer',
                'label': '',
                'width': 72,
                'height': 5,
                'render_format': 'html',
            },
        },
        'mailBodyHeader': {
            'type': 'Text Widget',
            'data': {
                'title': '',
                'fields': ('mailBodyHeader',),
                'label_edit': 'label_newsletter_mailbody_header',
                'is_i18n': 1,
                'width': 72,
                'height': 5,
                'render_format': 'html',
            },
        },
        'results': {
            'type': 'InternalLinks Widget',
            'data': {
                'title': '',
                'fields': ('results',),
                'is_required': False,
                'label_edit': 'label_newsletter_results',
                'is_i18n': True,
                'hidden_empty': False,
                'new_window': False,
                'size': 0,
            },
        },
    },
    'layout': {
        'style_prefix': 'layout_default_',
        'flexible_widgets': [],
        'ncols': 1,
        'rows': [
            [{'widget_id': 'mailBodyHeader', 'ncols': 1},
            ],
            [{'widget_id': 'results', 'ncols': 1},
            ],
            [{'widget_id': 'mailBodyFooter', 'ncols': 1},
            ],
        ],
    },
}

#######################################################
#######################################################

layouts = {}
layouts['newsletter'] = newsletter_layout

#######################################################
#######################################################

return layouts
