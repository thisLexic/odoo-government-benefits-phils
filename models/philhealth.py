from odoo import models, fields, api


class Philhealth(models.Model):
    _name = 'gov_bene_phils.philhealth'
    _description = 'Contains date and ref number for PhilHealth details'

    def name_get(self):
        result = []
        for record in self:
            date = record.date_contrib_end
            name = date.strftime("%B") + " " + date.strftime("%Y")
            result.append((record.id, name))
        return result


    @api.depends('date_contrib_end')
    def _get_month(self):
        for rec in self:
            rec.date_month = rec.date_contrib_end.strftime("%B")


    @api.depends('date_contrib_end')
    def _get_year(self):
        for rec in self:
            rec.date_year = rec.date_contrib_end.strftime("%Y")


    def _search_month(self, operator, value):
        if operator == "like":
            operator = "ilike"
            return [(self.date_month, operator, value)]


    def _search_year(self, operator, value):
        if operator == "like":
            operator = "ilike"
            return [(self.date_year, operator, value)]


    date_paid = fields.Date(string="Date Paid")
    date_contrib_start = fields.Date(string="Start Date")
    date_contrib_end = fields.Date(string="End Date")
    ref = fields.Char(string="Reference")
    transaction_number = fields.Char(string="Trans Num")
    # image_ids = fields.One2many('gov_bene_phils.sss_image', 'sss_id', string='Images')
    # emp_detl_ids = fields.One2many('gov_bene_phils.sss_employee_details', 'sss_id', string='Employee Benefits')
    company_id = fields.Many2one('res.company', string="Company/Employer")
    date_month = fields.Char(string="Month", compute="_get_month", search="_search_month", store=True)
    date_year = fields.Char(string="Year", compute="_get_year", search="_search_year", store=True)
    payment_medium = fields.Selection([('O', 'Online'), ('M', 'Manual')], string="Online/Manual")
    payment_method = fields.Selection([('cash', 'Cash'), ('check', 'Check')], string="Cash/Check")
    check_number = fields.Char(string="Check Number")
    check_date = fields.Date(string="Check Date")
    check_bank = fields.Char(string="Bank")
    check_branch = fields.Char(string="Branch Name")