{
    'name': 'IAP Client Service',
    'summary': 'IAP Client side configurations',
    'sequence': 100,
    'description': """
        IAP client side configurations and management
    """,
    'category': '',
    'author': 'bloopark systems GmbH & Co. KG',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/connect_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
