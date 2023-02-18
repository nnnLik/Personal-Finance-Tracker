from ninja import NinjaAPI
from src.user.api import router as user_router

api = NinjaAPI()

api.add_router("/user/", user_router)
