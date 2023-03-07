from odoo import fields,models

class Contacts(models.Model):
    _inherit = 'hr.contract'


    x_kpi_income = fields.Monetary('Lương KPI')
    x_overtime_income = fields.Monetary('Lương tăng ca')
    x_diligence = fields.Monetary('Chuyên cần')
    salary_per_month = fields.Monetary('Tiền công/tiền lương')
    sup_home = fields.Monetary('Hỗ trợ nhà ở')
    sup_gas = fields.Monetary('Hỗ trợ xăng xe')
    sup_food = fields.Monetary('Phụ cấp tiền ăn')
    sup_medical = fields.Monetary('Phụ cấp y tế')
    sup_other = fields.Monetary('Phụ cấp khác')
    sup_phone = fields.Monetary('Phụ cấp điện thoại')
    sup_da = fields.Monetary('DA')
    currency_id = fields.Many2one('res.currency', string='Tiền tệ', tracking=True,)
