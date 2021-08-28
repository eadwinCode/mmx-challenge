from .order import router as order_router
from ninja import NinjaAPI


api = NinjaAPI(title='Momox Test Project', urls_namespace='api')
api.add_router("/orders/", order_router, tags=['Orders'])
