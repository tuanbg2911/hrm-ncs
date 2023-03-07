from odoo import fields, models, api
import datetime
class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'

    number_people_deducted = fields.Integer('Số lượng người được giảm trừ', readonly=True, compute='_number_people_deducted')
    x_group_age = fields.Many2one('hr.employee.age')
    group_age = fields.Integer('Nhóm tuổi', readonly=True)
                               # , compute='_compute_group_age')
    age = fields.Many2one('hr.employee.age')
    x_dependent = fields.One2many('hr.employee.dependent', 'x_employee_id')

    @api.depends('x_dependent.x_reduce')
    def _number_people_deducted(self):
        lst = []
        for rec in self:
            if rec.x_dependent.x_reduce == True:
                lst.append(rec.x_dependent.x_reduce)
            rec.number_people_deducted = len(lst)


    # @api.depends('age.x_min_age')
    # def _compute_group_age(self):
    #     mylist = []
    #     for rec in self:
    #         years = datetime.datetime.now().year - rec.x_dependent.x_dob.year
    #         if years > rec.age.x_min_age:
    #             for i in range(0, years):
    #                 mylist.append(i)
                    # rec.group_age = min(mylist, key=lambda x: abs(x - years))

# Lấy ra 1 bản ghi thỏa mãn điều kiện: years > x_min_age  và  x_min_age gần years nhất.

