from odoo import models, fields
import requests
from urllib.parse import urljoin


class ServiceDBConnect(models.Model):
    _name = 'service.db.connect'
    _description = 'Connect Service Database'

    name = fields.Char(string='Service Name')
    contract_ref = fields.Char(string="Contract Reference")
    active = fields.Boolean(default=True)
    service_url = fields.Char()
    description = fields.Text()
    status = fields.Selection([
        ('failed', 'Failed'),
        ('success', 'Success')
    ])
    message = fields.Text()

    def get_service_end_point(self):
        # To return the end point
        end_point = self.env['ir.config_parameter'].sudo().\
            get_param("bloopark.end_point", False)
        return end_point

    def service_connect(self):
        # Connection to service DB for data
        status = 'failed'
        message = ''
        end_point = self.get_service_end_point()
        if end_point and self.contract_ref and self.service_url:
            try:
                params = dict(
                    contract_ref=self.contract_ref or ''
                )
                connect_url = urljoin(end_point, self.service_url)
                response = requests.get(url=connect_url, params=params)
                data = response.json()
                if data.get("success", False):
                    status = "success"

                message = data.get('message', "Failed to connect")
            except ValueError:
                status = "failed"
                message = 'Failed to connect'

        self.write({'status': status, 'message': message})
