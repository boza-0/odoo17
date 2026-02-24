{
    'name': 'Soluzion ID en Productos',
    'version': '17.0.1.0.0',
    'author': 'IWAN21',
    'category': 'Product',
    'summary': 'Añade el campo Soluzion_ID al producto',
    'description': """
Este módulo añade un campo personalizado Soluzion_ID
al modelo de productos para permitir la identificación
externa de los artículos mediante códigos alfanuméricos.
""",
    'depends': ['product'],
    'data': [
        'views/product_template_view.xml'
    ],
    'installable': True,
    'application': False,
}
