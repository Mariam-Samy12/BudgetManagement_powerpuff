from django.shortcuts import render
from django.db.models import Sum
from transactions.models import Transaction
from budgets.models import Budget
from goals.models import Goal
from django.contrib.auth.decorators import login_required
from decimal import Decimal
@login_required(login_url='login')
def dashboard_view(request):
  
    user_transactions = Transaction.objects.filter(user=request.user)

    total_income = user_transactions.filter(
        type='income'
    ).aggregate(Sum('amount'))['amount__sum'] or 0

    total_expense = user_transactions.filter(
        type='expense'
    ).aggregate(Sum('amount'))['amount__sum'] or 0

   
    total_balance = total_income - total_expense

    recent_transactions = user_transactions.order_by('-date')[:5]

    budgets = Budget.objects.filter(user=request.user)
    budget_alerts = []

    for b in budgets:
    
        spent = Transaction.objects.filter(
            user=request.user,
            category=b.category,
            type='expense',
            date__range=(b.start_date, b.end_date)
        ).aggregate(Sum('amount'))['amount__sum'] or 0

    
        # if b.amount > 0 and spent >= (b.amount * (b.alert_threshold / 100)):
        if b.amount > 0 and spent >= (b.amount * (Decimal(b.alert_threshold) / Decimal('100'))):
            budget_alerts.append({
                "budget": b,
                "spent": spent
            })

 
    # goals = Goal.objects.all()
    #i edited it <alaa mamdouh>
    goals = Goal.objects.filter(user=request.user)
    for goal in goals:
        goal.progress_bar = goal.calculate_progress()

    
    context = {
        'total_balance': total_balance,
        'income_summary': total_income,
        'expense_summary': total_expense,
        'recent_transactions': recent_transactions,
        'budget_alerts': budget_alerts,
        'goals_preview': goals,
    }

    return render(request, 'dashboard/dashboard.html', context)