##parameters=
#$Id$
"""Return the newsletters related layouts
"""

newsletter_layout = {
    'widgets': {
        'mailBodyFooter': {
            'type': 'Rich Text Editor Widget',
            'data': {
                'title': '',
                'fields': ('mailBodyFooter',),
                'is_required': False,
                'label': '',
                'label_edit': 'label_newsletter_mailbody_footer',
                'description': '',
                'help': '',
                'is_i18n': True,
                'readonly_layout_modes': (),
                'hidden_layout_modes': (),
                'hidden_readonly_layout_modes': (),
                'hidden_empty': False,
                'hidden_if_expr': '',
                'css_class': '',
                'widget_mode_expr': '',
                'width': 40,
                'height': 5,
            },
        },
        'mailBodyHeader': {
            'type': 'Rich Text Editor Widget',
            'data': {
                'title': '',
                'fields': ('mailBodyHeader',),
                'is_required': False,
                'label': '',
                'label_edit': 'label_newsletter_mailbody_header',
                'description': '',
                'help': '',
                'is_i18n': True,
                'readonly_layout_modes': (),
                'hidden_layout_modes': (),
                'hidden_readonly_layout_modes': (),
                'hidden_empty': False,
                'hidden_if_expr': '',
                'css_class': '',
                'widget_mode_expr': '',
                'width': 40,
                'height': 5,
            },
        },
        'results': {
            'type': 'InternalLinks Widget',
            'data': {
                'title': '',
                'fields': ('results',),
                'is_required': False,
                'label': 'label_newsletter_results',
                'label_edit': 'label_newsletter_results',
                'description': '',
                'help': '',
                'is_i18n': True,
                'readonly_layout_modes': (),
                'hidden_layout_modes': (),
                'hidden_readonly_layout_modes': (),
                'hidden_empty': False,
                'hidden_if_expr': '',
                'css_class': '',
                'widget_mode_expr': '',
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
