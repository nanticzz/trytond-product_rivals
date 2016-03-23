# This file is part product_rivals module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval
from trytond.modules.product import price_digits

__all__ = ['Template', 'Product', 'ProductRivals']


class Template:
    __name__ = 'product.template'
    __metaclass__ = PoolMeta

    list_price_supplier = fields.Property(fields.Numeric('List Price Supplier',
        states={
            'readonly': ~Eval('active', True),
            },
        digits=price_digits, depends=['active']))


class Product:
    __name__ = 'product.product'
    __metaclass__ = PoolMeta

    rivals = fields.One2Many('product.rivals',
            'product', 'Rivals')


class ProductRivals(ModelSQL, ModelView):
    'Product Rivals'
    __name__ = 'product.rivals'

    product = fields.Many2One('product.product',
        'Product', ondelete='CASCADE', required=True)
    name = fields.Char('Name', required=True)
    price = fields.Numeric('Price', digits=price_digits, required=True)
    app = fields.Many2One('product.app.rivals',
        'App', ondelete='CASCADE')

    @classmethod
    def __setup__(cls):
        super(ProductRivals, cls).__setup__()
        cls._order.insert(0, ('price', 'ASC'))
