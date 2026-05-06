from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from transactions.models import Transaction
from django.db.models import Sum


@login_required
def financial_report(request):

    
    user_transactions = Transaction.objects.filter(user=request.user)

    total_income = (
        user_transactions
        .filter(type='income')
        .aggregate(total=Sum('amount'))['total']
    ) or 0


    total_expense = (
        user_transactions
        .filter(type='expense')
        .aggregate(total=Sum('amount'))['total']
    ) or 0

   
    net_balance = total_income - total_expense

   
    category_data = (
        user_transactions
        .filter(type='expense')
        .values('category')
        .annotate(total=Sum('amount'))
        .order_by('-total')
    )

   
    context = {
        'total_income': total_income,
        'total_expense': total_expense,
        'net_balance': net_balance,
        'category_data': category_data,
    }

    return render(request, 'Reports & Analytics/Report.html', context)