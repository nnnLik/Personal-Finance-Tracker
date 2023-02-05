from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .serializers import GetUserFinanceSerializer

from .models import UserFinance


class UserFinanceView(ModelViewSet):
    """Display user information"""

    serializer_class = GetUserFinanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserFinance.objects.filter(id=self.request.user.id)
