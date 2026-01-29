{
    'name': 'Contact Discount Rate',
    'version': '1.0',
    'summary': 'Adds a special discount percentage to contacts',
    'depends': [
        'contacts',
        'sale',
        'product',
        'hr_contract',
        'project'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
        'views/sale_order_view.xml',
        'views/sale_category_view.xml',
        'views/product_template_view.xml',
        'views/hr_contract_view.xml',
        'views/project_task_view.xml'
    ],
    'installable': True,
    'application': False,
}
