from odoo import api, fields, models
class Insurance(models.Model):
    _name = "insurance"

    name = fields.Many2one("product.template", string="Tên sản phẩm")
    code = fields.Char("Mã sản phẩm")
    don_mua = fields.Many2one("sale.order", string="Đơn mua hàng")
    date = fields.Date("Ngày mua hàng")
    note = fields.Char("Lý do")
    free = fields.Boolean("Bảo hành miễn phí")
    mo_free = fields.Boolean("Bảo hành  tính phí")

    @api.onchange("name")
    def onchange_code(self):
        self.code = self.name.default_code

