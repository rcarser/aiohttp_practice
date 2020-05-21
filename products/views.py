# products/views.py

from aiohttp import web
from products.model import Product


class ProductView(web.View):

    async def get(self):
        """
        Product list and product details views.
        """
        match_info = self.request.match_info
        if 'product_id' in match_info:
            product = await Product.details(self.request.app['db'], match_info['product_id'])
            return product
        else:
            products = await Product.list(self.request.app['db'])
            return products

    async def post(self):
        """
        Product create view.
        """
        body = await self.request.json()
        product = await Product.create(self.request.app['db'], body)
        return product

    async def delete(self):
        """
        Product destroy view.
        """
        match_info = self.request.match_info
        if 'product_id' in match_info:
            product = await Product.delete(self.request.app['db'], match_info['product_id'])
            return product
