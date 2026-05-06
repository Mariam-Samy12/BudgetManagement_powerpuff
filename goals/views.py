from django.shortcuts import render, redirect
from .models import Goal
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def goals_list(request):
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'goals/goals_list.html', {'goals': goals})

@login_required(login_url='login')
def create_goal(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        target = request.POST.get('target_amount')
        deadline = request.POST.get('deadline')

        Goal.objects.create(
            user=request.user,
            name=name,
            target_amount=target,
            deadline=deadline
        )

        return redirect('goals_list')

    return render(request, 'goals/create_goal.html')