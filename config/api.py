from ninja import NinjaAPI
from src.user.api import router as user_router
from src.post.api import router as post_router

api = NinjaAPI()

api.add_router("/user/", user_router)
api.add_router("/post/", post_router)
