from ninja import NinjaAPI

from puissance4.adapters.http.api import router as puissance4_router

api = NinjaAPI()
api.add_router("/puissance4", puissance4_router)