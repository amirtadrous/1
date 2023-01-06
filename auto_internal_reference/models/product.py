# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Product(models.Model):
    _inherit = 'product.product'

    @api.model
    def create(self, vals_list):
        record = super().create(vals_list)
        if record.categ_id.product_sequence_id:
            next_code = record.categ_id.product_sequence_id.next_by_id()
            record.default_code = next_code
            if record.categ_id.apply_on_barcode:
                record.barcode = next_code
        return record
