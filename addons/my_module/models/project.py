from odoo import _, api, fields, models, tools


class Project(models.Model):
    _name = "project"
    _description = "The project of my module"
    # _order = 'sequence'

    name = fields.Char(string="Name", index=True)
    date_from = fields.Datetime(string="Start Date")
    date_to = fields.Datetime(string="End Date")
    user_id = fields.Many2one(comodel_name="res.users", string="Owner")
