from odoo import models, fields


class Company(models.Model):
    _inherit = "res.company"

    com_sss_num = fields.Char(string="SSS Number")
    com_philhealth_num = fields.Char(string="PhilHealth Number")
    com_pagibig_num = fields.Char(string="Pag-Ibig Number")