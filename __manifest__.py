{
    'name': 'Website Pay Mail',
    'version': '16.0.1.0.0',
    'description': "A mail will be sent to sales manager if a customer buys from shop",

    'depends': ['base', 'sale', 'website_sale'],
    'data': [
        'data/mail_template.xml'
    ],
}
