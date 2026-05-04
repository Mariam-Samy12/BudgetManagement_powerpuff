from django.shortcuts import render, redirect
from .models import Transaction


def add_transaction(request):
    if request.method == "POST":
        Transaction.objects.create(
            user=request.user,
            amount=request.POST['amount'],
            category=request.POST['category'],
            type=request.POST['type'],
            date=request.POST['date']
        )
        return redirect('Home')
    return render(request, 'transactions/add_transaction.html')