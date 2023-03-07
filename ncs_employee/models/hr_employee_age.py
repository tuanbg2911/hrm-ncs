from odoo import fields, models

class HrEmployeeAge(models.Model):
    _name = 'hr.employee.age'
    _description = 'Trang hiển thị tuổi nhân viên'

    x_name = fields.Char(string='Tên', required=True)
    x_min_age = fields.Integer(string='Tuổi tối thiểu', default=0)

class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'