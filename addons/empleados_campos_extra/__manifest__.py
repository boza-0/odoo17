{
    'name': 'Campos extra en empleados',
    'version': '1.0',
    'summary': 'Añade campos personalizados al modelo de empleados',
    'description': 'Módulo para añadir edad, fecha de revisión médica y grupo de puesto',
    'author': 'Ricardo Boza Villar',
    'category': 'Human Resources',
    'depends': ['hr'],  # Dependemos del módulo de empleados
    'data': [
        'views/hr_employee_view.xml',
    ],
    'installable': True,
    'application': False,
}
