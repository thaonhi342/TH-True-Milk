# -*- coding: utf-8 -*-
{
    'name': 'TH True Milk',
    'version': '1.0',
    'author': '',
    'maintainer': '',
    'website': '',

    'description': """ """,
    'depends': ['base',"mail" ,"portal", "product","sale","hr"],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        "views/product_view.xml",
        "views/sale_oder.xml",
        "views/hr_employee.xml",
        "views/insurance.xml"
    ],
    'qweb': [],
    'installable': True,
    'auto_install': False,
}
