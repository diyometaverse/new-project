from django.shortcuts import render

from transaction.models import Transaction
from django.shortcuts import render
from django.db.models import Sum
from django.utils.html import escape
# Create your views here.

def index(request):
    return render(request, 'landing_page.html')

def transaction_page(request):
    # Last 10 transactions ordered by timestamp
    transactions = (
        Transaction.objects
        .filter(user=request.user)
        .order_by('-timestamp')[:10]
        .values('timestamp', 'amount')
    )

    total_transactions = Transaction.objects.filter(user=request.user).count()
    total_amount = (
        Transaction.objects
        .filter(user=request.user)
        .aggregate(total=Sum('amount'))['total'] or 0
    )

    # Sanitize and format timestamp
    safe_transactions = [
        {
            'timestamp': t['timestamp'].strftime('%Y-%m-%d %H:%M:%S'),
            'amount': t['amount'],
        }
        for t in transactions
    ]

    context = {
        'user': request.user,
        'transactions': safe_transactions,
        'total_transactions': total_transactions,
        'total_income': total_amount,   # Reuse total_amount for display
        'total_expense': 0,             # No type field to separate
    }

    return render(request, 'dashboard.html', context)

def add_transaction(request):
    return render(request, 'add_transaction.html')

def save_transaction(request):
    if request.method == 'POST':
        user = request.user
        amount = request.POST.get('amount')
        
        transaction = Transaction(
            user=user,
            amount=amount
        )
        transaction.save()
        
    transactions = Transaction.objects.filter(user=request.user).order_by('-timestamp')
    
    return render(request, 'dashboard.html', {'transactions': transactions})