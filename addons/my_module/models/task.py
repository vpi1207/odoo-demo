from odoo import _, api, fields, models, tools
from datetime import timedelta


class Task(models.Model):
    _name = "task"
    _description = "The project tasks"

    name = fields.Char(string="Name", required=True, index=True)
    project_id = fields.Many2one(comodel_name="project", string="Project")
    user_id = fields.Many2one("res.users", string="Assignee")
    date_due = fields.Date(string="Due Date", default=lambda s: fields.Date.context_today(s) + timedelta(days=7))
