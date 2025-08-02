from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ExpenseViewSet, check_expense_limit
from django.urls import path, include

router = DefaultRouter()
router.register(r'User', UserViewSet)
router.register(r'Event', ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/<int:user_id>/check-expense-limit/', check_expense_limit),

   
]