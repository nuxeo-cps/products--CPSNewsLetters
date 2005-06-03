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
           'type': 'CPS NewsLetter InternalLinks Widget',
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
        'query_fulltext': {
            'type': 'String Widget',
            'data': {
                'fields': ('query_fulltext'),
                'is_i18n': 1,
                'label_edit': 'label_search_full_text',
                'display_width': 40,
                'size_max': 100,
            },
        },
        'query_title': {
            'type': 'String Widget',
            'data': {
                'fields': ('query_title'),
                'is_i18n': 1,
                'label_edit': 'label_search_title',
                'display_width': 40,
                'size_max': 100,
            },
        },
        'query_description': {
            'type': 'String Widget',
            'data': {
                'fields': ('query_description'),
                'is_i18n': 1,
                'label_edit': 'label_search_description',
                'display_width': 40,
                'size_max': 100,
            },
        },
        'folder': {
            'type': 'String Widget',
            'data': {
                'fields': ('folder'),
                'is_i18n': 1,
                'label_edit': 'label_folder',
                'display_width': 40,
                'size_max': 100,
            },
        },
        'nb_items': {
            'type': 'Int Widget',
            'data': {
                'fields': ('nb_items'),
                'is_i18n': 1,
                'label_edit': 'label_nb_items',
                'display_width': 3,
            },
        },
        'sort_by': {
            'type': 'Select Widget',
            'data': {
                'fields': ['sort_by'],
                'is_i18n': 1,
                'label_edit': 'label_sort_by',
                'vocabulary': 'search_sort_results_by',
                'translated': 1,
                },
            },
        'query_status': {
            'type': 'Select Widget',
            'data': {
                'fields': ['query_status'],
                'is_i18n': 1,
                'label_edit': 'label_search_status',
                'vocabulary': 'navigation_filter_review_state',
                'translated': 1,
                },
            },
        'query_portal_type': {
            'type': 'MultiSelect Widget',
            'data': {
                'fields': ['query_portal_type'],
                'is_i18n': 1,
                'label_edit': 'label_search_portal_type',
                'vocabulary': 'navigation_filter_listing_ptypes',
                'size': 10,
                },
            },
        'search': {
            'type': 'Search Widget',
            'data': {
                'fields': (),
                'label_edit': 'label_search',
                'help': 'help_newsletter_search_widget',
                'is_i18n': 1,
                'css_class': 'articleELink',
                'widget_ids': ['query_fulltext',
                               'query_title', 'query_description',
                               'query_status', 'query_portal_type',
                               'folder', 'nb_items', 'sort_by'],
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
            [{'widget_id': 'search', 'ncols': 1},
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
