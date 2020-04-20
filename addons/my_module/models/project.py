from odoo import _, api, fields, models, tools


class Project(models.Model):
    _name = "project"
    _description = "The project of my module"
    _order = "date_from"

    name = fields.Char(string="Name", index=True)
    date_from = fields.Datetime(string="Start Date", required=True)
    date_to = fields.Datetime(string="End Date")
    user_id = fields.Many2one(comodel_name="res.users", string="Owner")
    state = fields.Selection(
        selection=[("progress", "In Progress"), ("approved", "Approved"), ("rejected", "Rejected")],
        string="Status",
        default="progress",
    )
    tag_ids = fields.Many2many("project.tag", string="Custom Tags",)

    def action_approve(self):
        for project in self:
            project.state = "approved"


class ProjectTag(models.Model):
    _name = "project.tag"
    _description = "The tags"

    name = fields.Char(required=True)
    color = fields.Integer(string="Color Index")

    _sql_constraints = [("name_uniq", "unique (name)", "Tag name already exists!")]
