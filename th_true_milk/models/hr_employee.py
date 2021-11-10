from odoo import fields, models, api,_
from odoo.exceptions import ValidationError

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    code = fields.Char(string="Mã nhân viên" , required=True)

    @api.constrains('code')
    def _check_default_code(self):
        exists = self.env['hr.employee'].search(
            [('code', '=', self.code), ('id', '!=', self.id)])
        if exists:
            raise ValidationError(_('Mã nhân viên ' + self.code + ' đã tồn tại.'))