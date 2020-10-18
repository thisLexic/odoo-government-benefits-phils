# -*- coding: utf-8 -*-
import datetime
from odoo import models, fields, api

# import logging
# _logger = logging.getLogger(__name__)


class Sss(models.Model):
    _name = 'gov_bene_phils.sss'
    _description = 'Contains date and ref number for SSS details'


    def name_get(self):
        result = []
        for record in self:
            date = record.applicable_date
            try:
                name = date.strftime("%B") + " " + date.strftime("%Y")
            except:
                name = "Date Not Set"
            result.append((record.id, name))
        return result


    @api.depends('applicable_year', 'applicable_month')
    def _get_date(self):
        for rec in self:
            try:
                rec.applicable_date = datetime.datetime(int(rec.applicable_year), int(rec.applicable_month), 1)
            except:
                pass

    @api.depends('company_id')
    def _get_sss_id(self):
        for rec in self:
            rec.company_sss = rec.company_id.com_sss_num


    def _default_currency_id(self):
         return self.env['res.currency'].search([('name', '=', 'PHP')], limit=1).id


    date_paid = fields.Date(string="Date Paid")
    applicable_date = fields.Date(string="Applicable Date", compute="_get_date", search="_search_date", store=True)
    applicable_month = fields.Selection([('1', 'Jan'), ('2', 'Feb'), ('3', 'Mar'), ('4', 'Apr'), ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'Aug'), ('9', 'Sept'), ('10', 'Oct'), ('11', 'Now'), ('12', 'Dec')], string='Month')
    applicable_year = fields.Selection([('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ], string='Year')
    ref = fields.Char(string="Reference")
    transaction_number = fields.Char(string="Trans Num")
    image_ids = fields.One2many('gov_bene_phils.sss_image', 'sss_id', string='Images')
    emp_detl_ids = fields.One2many('gov_bene_phils.sss_employee_details', 'sss_id', string='Employee Benefits')
    company_id = fields.Many2one('res.company', string="Company/Employer")
    company_sss = fields.Char(string="SSS ID", compute="_get_sss_id")
    payment_medium = fields.Selection([('O', 'Online'), ('M', 'Manual')], string="Online/Manual")
    payment_method = fields.Selection([('cash', 'Cash'), ('check', 'Check')], string="Cash/Check")
    check_number = fields.Char(string="Check Number")
    check_date = fields.Date(string="Check Date")
    check_bank = fields.Char(string="Bank")
    check_branch = fields.Char(string="Branch Name")
    currency_id = fields.Many2one('res.currency', string="Currency", default=_default_currency_id)
    amount = fields.Monetary(string="Amount")



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

    @api.depends('emp_id')
    def _get_sss_id(self):
        for rec in self:
            rec.emp_sss_id = rec.emp_id.emp_sss_num

    def _default_currency_id(self):
         return self.env['res.currency'].search([('name', '=', 'PHP')], limit=1).id


    sss_id = fields.Many2one('gov_bene_phils.sss', string="SSS Payment")
    currency_id = fields.Many2one('res.currency', string="Currency", default=_default_currency_id)
    emp_id = fields.Many2one('hr.employee', string="Employee")
    emp_sss_id = fields.Char(string="SSS ID", compute="_get_sss_id")
    emp_contrib = fields.Monetary(string="Employee Contribution")
    comp_contrib = fields.Monetary(string="Owner Contribution")
    ec_contrib = fields.Monetary(string="EC Contribution")

