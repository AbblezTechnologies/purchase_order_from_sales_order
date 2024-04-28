# -*- coding: utf-8 -*-
{
    'name': 'Customize Purchase Order',
    'version': '1.0',
    'summary': 'Create purchase order from  Sale order lines based on Vendor selection',
    'author': 'Rosmi',
    'description': """Create purchase order from  Sale order lines based on Vendor selection""",
    'depends': ['base', 'product', 'sale', 'purchase'],
    'assets': {
        'web.assets_frontend': [

        ],
    },
    'data': [
        'views/sale_order_inherit_views.xml'
    ],
    'licenSe': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False
}
