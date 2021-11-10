from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    phone=fields.Char("Điện thoại" )
    sdt=fields.Char("Di động")
    address=fields.Char("Địa chỉ giao hàng")

    @api.onchange('partner_id')
    def get_phone(self):
        self.phone = self.partner_id.phone

    @api.onchange('partner_id')
    def get_sdt(self):
        self.sdt = self.partner_id.mobile




