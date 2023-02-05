from django.urls import path
from . import views

urlpatterns = [
    path(
        "user/<int:pk>/",
        views.UserFinanceView.as_view({"get": "retrieve", "put": "update"}),
    ),
]
