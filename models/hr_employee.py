from odoo import models, fields


class Employee(models.Model):
    _inherit = "hr.employee"

    emp_sss_detl_ids = fields.One2many('gov_bene_phils.sss_employee_details', 'emp_id', string='SSS Benefits')
    emp_sss_num = fields.Char(string="SSS Number")
    emp_philhealth_detl_ids = fields.One2many('gov_bene_phils.philhealth_employee_details', 'emp_id', string='PhilHealth Benefits')
    emp_philhealth_num = fields.Char(string="PhilHealth Number")
    emp_pagibig_detl_ids = fields.One2many('gov_bene_phils.pagibig_employee_details', 'emp_id', string='Pag-Ibig Benefits')
    emp_pagibig_num = fields.Char(string="Pag-Ibig Number")