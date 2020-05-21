# routes.py

from products.views import ProductView

def routes(app):
    """
    Define application routes using Class Based Views.
    """
    app.router.add_view('/products', ProductView)
    app.router.add_view('/products/{product_id}', ProductView)
