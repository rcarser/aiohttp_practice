# main.py

from aiohttp import web

from routes import routes
from db import db_init


if __name__ == '__main__':
    app = web.Application()
    routes(app)
    db_init(app)
    web.run_app(app)
