from odoo import models, fields


class Company(models.Model):
    _inherit = "res.company"

    com_sss_num = fields.Char(string="SSS Number")