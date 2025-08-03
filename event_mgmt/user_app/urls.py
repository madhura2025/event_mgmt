from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ExpenseViewSet, check_expense_limit, monthly_expenseSummary_byCategoty, expense_per_day, top_spending_category
from django.urls import path, include

router = DefaultRouter()
router.register(r'User', UserViewSet)
router.register(r'Event', ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/<int:user_id>/check-expense-limit/', check_expense_limit),
    path('user/<int:user_id>/monthlyexp/',monthly_expenseSummary_byCategoty),
    path('user/<int:user_id>/expense_per_day/',expense_per_day),
    path('user/<int:user_id>/top_spending_category/',top_spending_category),

    



   
]