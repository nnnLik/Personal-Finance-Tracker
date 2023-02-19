from src.user.models import UserFinance


class FinanceUserService:
    def get_users(self):
        users = UserFinance.objects.all()
        return users


user_services = FinanceUserService()
