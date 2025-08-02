from rest_framework import viewsets
from rest_framework.response import Response
from .models import User, Expense
from .serializers import UserSerializer, ExpenseSerializer
from rest_framework.decorators import api_view

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

@api_view(['GET'])
def check_expense_limit(request, user_id):
    user = User.objects.get(id=user_id)
    total_expenses = Expense.objects.filter(user_id=user).values_list('expense_amount', flat=True)
    total_expenses = sum(int(amount) for amount in total_expenses if amount is not None)
    over_limit = total_expenses > user.salary
    message = "You have exceeded your salary limit!" if over_limit else "You're within your budget."
    return Response(
        {
            "salary":user.salary,
            "total_expenses":total_expenses,
            "over_limit":over_limit,
            "message":message
        }
    )
