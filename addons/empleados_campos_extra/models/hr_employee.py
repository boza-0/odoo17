from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'  # Heredamos del modelo de empleados

    # Campo entero para la edad del empleado
    edad = fields.Integer(
        string='Edad',
        help='Edad del empleado'
    )

    # Campo fecha para la próxima revisión médica
    fecha_revision_medica = fields.Date(
        string='Próxima revisión médica',
        help='Fecha de la próxima revisión médica del empleado'
    )

    # Campo selección para el grupo del puesto de trabajo
    grupo_puesto = fields.Selection(
        [
            ('administrativo', 'Administrativo'),
            ('tecnico', 'Técnico'),
            ('otros', 'Otros'),
        ],
        string='Grupo del puesto',
        help='Grupo al que pertenece el puesto de trabajo'
    )
