from odoo import fields, models
import datetime
class HrEmployeeDependent(models.Model):
    _name = 'hr.employee.dependent'
    _description = 'Trang nhân viên'


    x_name = fields.Char('Tên')
    x_dob = fields.Date('Ngày sinh')
    x_reduce = fields.Boolean('Được giảm trừ gia cảnh')
    x_employee_id = fields.Many2one('hr.employee', string='Nhân viên')
