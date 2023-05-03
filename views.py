from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm   
from .models import *
from django.views.generic import ListView


@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('transaction_list')

    else:
        form = TransactionForm()
    return render(request, 'transactions/ttransaction_form.html', {'form': form})
@login_required()


class TransactionListView(ListView):
    model = Transaction
    template_name = 'financeapp/transaction_list.html'

def my_view(request):
    return render(request, 'myapp/template.html')




