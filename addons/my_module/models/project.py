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
    task_ids = fields.One2many(comodel_name="task", inverse_name="project_id", string="Tasks")
    duration = fields.Float(string="Duration", compute="_compute_duration")

    @api.depends('date_from', 'date_to')
    def _compute_duration(self):
        for project in self:
            if project.date_from and project.date_to:
                project.duration = ((project.date_to - project.date_from).total_seconds()) / (24 * 60 * 60)

    def action_approve(self):
        for project in self:
            project.state = "approved"


class ProjectTag(models.Model):
    _name = "project.tag"
    _description = "The tags"

    name = fields.Char(required=True)
    color = fields.Integer(string="Color Index")

    _sql_constraints = [("name_uniq", "unique (name)", "Tag name already exists!")]
