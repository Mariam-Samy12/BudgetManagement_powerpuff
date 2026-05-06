from django.shortcuts import render, redirect
from .models import Transaction
from goals.models import Goal
from django.contrib.auth.decorators import login_required
from decimal import Decimal
@login_required(login_url='login')
def add_transaction(request):
    if request.method == "POST":
        #goals
        goal_id = request.POST.get('goal')
        selected_goal = Goal.objects.filter(id=goal_id).first() if goal_id else None

        Transaction.objects.create(
            user=request.user,
            amount=request.POST['amount'],
            category=request.POST['category'],
            type=request.POST['type'],
            date=request.POST['date'],
            #goal
            goal=selected_goal
        )

        #goal
        if selected_goal and request.POST['type'] == 'Saving':
         selected_goal.current_amount += Decimal(request.POST['amount'])
         selected_goal.save()

        return redirect('/dashboard/')
    user_goals = Goal.objects.filter(user=request.user)
    return render(request, 'transactions/add_transaction.html', {'goals': user_goals})