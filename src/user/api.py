from typing import List
from django.http import HttpRequest

from ninja import Router
from asgiref.sync import sync_to_async

from src.user.models import UserFinance
from src.user.schemas import UserFinancePublicSchema, UserFinancePrivateSchema

from src.user.services import user_services

router = Router()


@router.get(
    "/public",
    response=List[UserFinancePublicSchema],
)
async def list_users(request: HttpRequest):
    users = user_services.get_users()
    return await sync_to_async(list)(users)


@router.get(
    "/private",
    response=List[UserFinancePrivateSchema],
)
async def list_users(request: HttpRequest):
    users = user_services.get_users()
    return await sync_to_async(list)(users)
