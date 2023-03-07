{
    'name': "ncs_employee",
    'depends': ['base','hr'],
    'data': [
        'views/contact.xml',
        'views/hr_employee_dependent.xml',
        'views/hr_employee_age.xml',
        'views/hr_plan.xml',
        'views/hr_employee_inherit.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',

    ]

}