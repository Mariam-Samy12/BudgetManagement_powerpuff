from django.shortcuts import render, redirect
from .models import Transaction
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def add_transaction(request):
    if request.method == "POST":
        Transaction.objects.create(
            user=request.user,
            amount=request.POST['amount'],
            category=request.POST['category'],
            type=request.POST['type'],
            date=request.POST['date']
        )
        return redirect('/dashboard/')
    return render(request, 'transactions/add_transaction.html')