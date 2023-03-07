from odoo import fields,models

class Contacts(models.Model):
    _name = 'contact'

    x_kpi_income = fields.Monetary('Lương KPI')
    x_overtime_income = fields.Monetary('Lương tăng ca')
    x_diligence = fields.Monetary('Chuyên cần')
    currency_id = fields.Many2one('res.currency', string='Tiền tệ', tracking=True,)