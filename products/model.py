from aiohttp import web
from bson.objectid import ObjectId
from typing import Optional
from pydantic import BaseModel, Field


class Product(BaseModel):
    """
    Product model.
    """
    id: Optional[str]
    title: str = ...
    description: str
    genre: str 
    brand: str 
    category: str
    color: str
    price: float = ...

    @staticmethod
    async def details(db, product_id):
        """
        Get a specific product.
        """
        try:
            qs = await db.products.find_one({'_id': ObjectId(product_id)})
            qs['id'] = str(qs['_id'])
            qs.pop('_id')
            product = Product(**qs).dict()
            return web.json_response(product, status=200, content_type='application/json')
        except:
            response = [{'message': f'Impossible retrieve product [{product_id}] from database'}]
            return web.json_response(response, status=403, content_type='application/json')

    @staticmethod
    async def list(db):
        """
        Get the last twenty products.
        """
        qs = db.products.find()
        products = []
        for p in await qs.to_list(length=20):
            p['id'] = str(p['_id'])
            product = Product(**p).dict()
            products.append(product)
        return web.json_response(products, status=200, content_type='application/json')

    @staticmethod
    async def create(db, data):
        """
        Create product into db.
        """
        try:
            product = Product(**data).dict()
            qs = await db.products.insert_one(data)
            product['id'] = str(qs.inserted_id)
            return web.json_response(product, status=201, content_type='application/json')
        except:
            response = [{'message': 'Impossible save product in database'}]
            return web.json_response(response, status=403, content_type='application/json')

    @staticmethod
    async def delete(db, product_id):
        """
        Remove product from db.
        """
        try:
            qs = await db.products.delete_one({'_id': ObjectId(product_id)})
            response = [{'message': f'Product with id [{product_id}] was successfully removed.'}]
            return web.json_response(response, status=200, content_type='application/json')
        except:
            response = [{'message': f'Impossible remove product with id [{product_id}]'}]
            return web.json_response(response, status=403, content_type='application/json')
