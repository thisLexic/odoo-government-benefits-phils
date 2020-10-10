# -*- coding: utf-8 -*-
{
    'name': "Gov't Benefits - Philippines",

    'summary': """
        Manage government benefits such as SSS, PhilHealth, and Pag-Ibig payments of employees in the Philippines.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'views/sss.xml',
        'views/philhealth.xml',
        'views/hr_employee.xml',
        'views/res_company.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
