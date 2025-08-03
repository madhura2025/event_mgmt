from rest_framework import viewsets
from rest_framework.response import Response
from .models import User, Expense
from .serializers import UserSerializer, ExpenseSerializer
from rest_framework.decorators import api_view
from django.db.models import Sum
from datetime import datetime


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

@api_view(['GET'])
def monthly_expenseSummary_byCategoty(request, user_id):
    user = User.objects.get(id=user_id)
    categories = ['NEED', 'LUXURY', 'INVESTMENT']
    summary = {}

    for cat in categories:
        total = Expense.objects.filter(user_id=user, category=cat).aggregate(
            total_amount=Sum('expense_amount')
        )['total_amount'] or 0
        summary[cat] = total

    return Response({
        "user": user.fname,
        "category_summary": summary})

@api_view(['GET'])
def expense_per_day(request, user_id):
    user = User.objects.get(id=user_id)
    daily_spending = Expense.objects.filter(user_id=user_id).values('date').annotate(daily_total=Sum('expense_amount'))
    return Response({'User':user.fname,
                     'daily_spending':daily_spending})

@api_view(['GET'])
def top_spending_category(request, user_id):
    user = User.objects.get(id=user_id)
    top_spending_cat = Expense.objects.filter(user_id=user_id, date__month=datetime.now().month, date__year=datetime.now().year).values('category').annotate(total_spend=Sum('expense_amount')).order_by('-total_spend').first()
    return Response({
        'user': user.fname,
        'Monthly and yearly top spending category':top_spending_cat
    })