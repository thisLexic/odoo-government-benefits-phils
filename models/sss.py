# -*- coding: utf-8 -*-

from odoo import models, fields, api

# import logging
# _logger = logging.getLogger(__name__)


class Sss(models.Model):
    _name = 'gov_bene_phils.sss'
    _description = 'Contains date and ref number for SSS details'


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
    image_ids = fields.One2many('gov_bene_phils.sss_image', 'sss_id', string='Images')
    emp_detl_ids = fields.One2many('gov_bene_phils.sss_employee_details', 'sss_id', string='Employee Benefits')
    company_id = fields.Many2one('res.company', string="Company/Employer")
    date_month = fields.Char(string="Month", compute="_get_month", search="_search_month", store=True)
    date_year = fields.Char(string="Year", compute="_get_year", search="_search_year", store=True)
    payment_medium = fields.Selection([('O', 'Online'), ('M', 'Manual')], string="Online/Manual")
    payment_method = fields.Selection([('cash', 'Cash'), ('check', 'Check')], string="Cash/Check")
    check_number = fields.Char(string="Check Number")
    check_date = fields.Date(string="Check Date")
    check_bank = fields.Char(string="Bank")
    check_branch = fields.Char(string="Branch Name")



class Image(models.Model):
    _name = 'gov_bene_phils.sss_image'
    _description = 'Contains images of SSS details'


    @api.depends('image')
    def _get_preview(self):
        self.preview = self.image


    def _get_image_html(self):
        for elem in self:
            attachment = self.env['ir.attachment'].search(
                [('res_model', '=', 'gov_bene_phils.sss_image'),
                ('res_id', '=', self.id)], limit=1
                )
            image_url = "/web/image/ir.attachment/%s/datas" % attachment.id
            elem.image_loc = '<img src="%s"/>' % image_url


    sss_id = fields.Many2one('gov_bene_phils.sss', string="SSS Payment")
    # label = fields.Char(string="Label")
    custom_label = fields.Many2one('gov_bene_phils.sss_image_label', string='Label')
    image = fields.Binary(string="Image")
    preview = fields.Binary(string="Preview", compute="_get_preview")
    image_loc = fields.Html(string='Preview 2', compute="_get_image_html")


class Label(models.Model):
    _name = 'gov_bene_phils.sss_image_label'
    _description = 'Contains labels for SSS images'

    name = fields.Char(string="Name")
    image_ids = fields.One2many('gov_bene_phils.sss_image', 'custom_label', string='Images')


class Sss_Employee_Details(models.Model):
    _name = 'gov_bene_phils.sss_employee_details'
    _description = 'Contains employee payment details of SSS transaction'


    def _default_currency_id(self):
         return self.env['res.currency'].search([('name', '=', 'PHP')], limit=1).id


    sss_id = fields.Many2one('gov_bene_phils.sss', string="SSS Payment")
    currency_id = fields.Many2one('res.currency', string="Currency", default=_default_currency_id)
    emp_id = fields.Many2one('hr.employee', string="Employee")
    emp_contrib = fields.Monetary(string="Employee Contribution")
    comp_contrib = fields.Monetary(string="Owner Contribution")
    ec_contrib = fields.Monetary(string="EC Contribution")

