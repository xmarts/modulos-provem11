# -*- coding: utf-8 -*-
{
    'name': "Customize SLI",

    'summary': """
       Personalizaciones""",

    'description': """
   Personalizaciones para SLI
    """,

    'author': "Luis Alfredo Valencia Díaz, modificado por Pablo Osorio",
    'website': "http://www.xmarts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','hr_applicant_recruitment'],
    # always loaded
    'data': [
       'security/ir.model.access.csv',
       'views/views.xml',
        'reports/layout.xml',
       'reports/report_contract_sli.xml',
    'reports/report_contract_quetzal.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
