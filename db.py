# db.py

from motor import motor_asyncio

async def start_db(app):
    uri = 'mongodb://mongo:mongo@db:27017'
    db = motor_asyncio.AsyncIOMotorClient(uri)['aiohttp_shop']
    app['db'] = db

async def close_db(app):
    pass

def db_init(app):
    app.on_startup.append(start_db)
    app.on_cleanup.append(close_db)
