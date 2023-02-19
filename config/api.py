from ninja import NinjaAPI

from src.user.api import router as user_router
from src.bank.api import router as bank_router

api = NinjaAPI(
    title="Persomal Finance Tracker", version="1.0.1", urls_namespace="main_api"
)

api.add_router("/user/", user_router)
api.add_router("/bank/", bank_router)
