from odoo import models, fields


class Employee(models.Model):
    _inherit = "hr.employee"

    emp_sss_detl_ids = fields.One2many('gov_bene_phils.sss_employee_details', 'emp_id', string='SSS Benefits')
    emp_sss_num = fields.Char(string="SSS Number")