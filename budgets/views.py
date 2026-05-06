from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Budget
from django.contrib.auth.decorators import login_required
from datetime import datetime


@login_required(login_url='login')
def manage_budget(request, pk=None):
   
    budget_instance = get_object_or_404(Budget, pk=pk, user=request.user) if pk else None

    if request.method == 'POST':
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        alert = request.POST.get('alert_threshold')
        
       
        if start_date >= end_date:
            messages.error(request, "Error: The end date must be after the start date!")
            return render(request, 'budgets/create_budget.html', {
                'budget': budget_instance,
            })

      
        if not pk:
            start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
            exists = Budget.objects.filter(
                user=request.user, 
                category=category, 
                start_date__month=start_date_obj.month,
                start_date__year=start_date_obj.year
            ).exists()

            if exists:
                messages.warning(request, f"You already have a budget for '{category}' this month!")
                return redirect('budget_home')


        if budget_instance:
            budget_instance.category = category
            budget_instance.amount = amount
            budget_instance.start_date = start_date
            budget_instance.end_date = end_date
            budget_instance.alert_threshold = alert
            budget_instance.save()
            messages.success(request, "Budget updated successfully!")
        else:
            Budget.objects.create(
                user=request.user, category=category, amount=amount,
                start_date=start_date, end_date=end_date, alert_threshold=alert
            )
            messages.success(request, "Budget created successfully!")
        
        return redirect('budget_home')

    return render(request, 'budgets/create_budget.html', {'budget': budget_instance})


@login_required(login_url='login')
def budget_home(request):
    user_budgets = Budget.objects.filter(user=request.user).order_by('-start_date')
    return render(request, 'budgets/budget_home.html', {'budgets': user_budgets})