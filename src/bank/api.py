from typing import List
from django.http import HttpRequest

from ninja import Router
from asgiref.sync import sync_to_async

router = Router()
