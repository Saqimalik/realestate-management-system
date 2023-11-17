# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Real Estate',
    'version': '1.2',
    'summary': 'Real Estate managenment software',
    'author': 'Your Name',
    'description': """Real Estate managenment software""",
    'sequence': -100,
    'category': 'Productivity/Discuss',
    'website': 'http://www.odoomates.tech',
    'license': 'LGPL-3',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate.xml' ,
        'views/sale.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
