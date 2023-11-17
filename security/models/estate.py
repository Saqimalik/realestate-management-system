# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class Real_Estate(models.Model):
    _name = "real.estate"
    _description = "Real estate"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', required=True)
    gender = fields.Selection([
        ('male', 'male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')
    note = fields.Text(string='Description')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], default='draft', string="status")

    responsible_id = fields.Many2one('res.company', string="Responsible")

    def action_done(self):
        self.state = 'done'

    def action_confirm(self):
        self.state = 'confirm'

    def action_draft(self):
        self.state = 'draft'

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['note'] = self.env['ir.sequence'].next_by_code('real.estate.sequence') or _('New')
        result = super(Real_Estate, self).create(vals)
        return result

    # @api.onchange('estate_id')
    # def set_estate_gender(self):
    #     for rec in self:
    #         if rec.doctor_id:
    #             rec.doctor_gender = rec.estate_id.gender
