from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo import http
from odoo.http import request


class WebsitePayMail(WebsiteSale):
    @http.route()
    def shop_payment_confirmation(self, **post):
        res = super(WebsitePayMail, self).shop_payment_confirmation(**post)
        print('kkkkkkkk', request.website.sale_get_order())
        sale_order_id = request.session.get('sale_last_order_id')
        sale_order = request.env['sale.order'].browse(sale_order_id)
        values = {
            'id': sale_order.id,
            'customer': sale_order.partner_id.name,
            'sale_order_no': sale_order.name,
            'total_amount': sale_order.amount_total,
            'order_line': sale_order.order_line,
        }
        print(sale_order_id)
        mail_template = request.env.ref('website_pay_mail.mail_pay')
        mail_template.with_context(values).sudo().send_mail(request.session.get('sale_last_order_id'),
                                                            force_send=True)
        return res


