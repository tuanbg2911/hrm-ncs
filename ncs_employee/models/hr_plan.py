from odoo import fields, models

class HrPlan(models.TransientModel):
    _inherit = 'hr.plan.wizard'
    _description = 'Trang kế hoạch'

    name = fields.Char('Tên')