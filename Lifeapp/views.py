from django.shortcuts import render, redirect
from . models import FinancialRecord, BankStatement, Expense, Account,Voucher,GeneralLedger
from django.views import View
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login') 

# Create your views here.
def custom_login(request):
    icon_url = "http://danielzawadzki.com/codepen/01/icon.svg"
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Use the renamed login function
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'Login.html', {'icon_url': icon_url})

@login_required
def base(request):
    return render(request,'base.html')
@login_required
def index(request):
    return render(request,'index.html')
@login_required
def ledger(request):
    Generalledger = GeneralLedger.objects.all()
    
    context = {
        'Generalledger' : Generalledger
    }
    
    return render(request,'ledger.html', context)

@login_required
def financebook(request):   
    
    
    financial_transactions = FinancialRecord.objects.all()
    
     
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        if start_date and end_date:
            financial_transactions = FinancialRecord.objects.filter(date__range=[start_date, end_date])
        
    
    financial_transactions = financial_transactions.order_by('date')
    
    
    opening_financial_balance = financial_transactions.first().balance if financial_transactions else 0
    closing_financial_balance = financial_transactions.last().balance if financial_transactions else 0
    closing_balance = closing_financial_balance
    
    context ={ 
              'financial_transactions' : financial_transactions,
              'opening_financial_balance' : opening_financial_balance,
              'closing_financial_balance' : closing_financial_balance,
              'closing_balance' : closing_balance,
            }
    return render(request,'financebook.html', context)
@login_required
def bank(request):
    bank_transactions = BankStatement.objects.all()
    
    if request.method == 'POST':
        start_date = request.POST.get('startdate')
        end_date = request.POST.get('enddate')
        
        
        if start_date and end_date:
            bank_transactions = BankStatement.objects.filter(date__range=[start_date, end_date])
              
    # Calculate opening and closing balance for bank transactions
    opening_bank_balance = bank_transactions.first().balance if bank_transactions else 0
    closing_bank_balance = bank_transactions.last().balance if bank_transactions else 0
    
    
    
    context = { 
               'bank_transactions' : bank_transactions,
               'opening_bank_balance' : opening_bank_balance,
               'closing_bank_balance': closing_bank_balance,
               
               
        
    }
    
    return render(request,'bank.html', context)
@login_required
def reconcile(request):
    
    financial_transactions = FinancialRecord.objects.all()
    bank_transactions = BankStatement.objects.all()
    
    show_reconciliation = False
    
    
    if request.method == 'POST':
        start_date = request.POST.get('startdate')
        end_date = request.POST.get('enddate')
        
        show_reconciliation = True
        
        if start_date and end_date:
            bank_transactions = BankStatement.objects.filter(date__range=[start_date, end_date])
            financial_transactions = FinancialRecord.objects.filter(date__range=[start_date, end_date])
    
    
    
    opening_financial_balance = financial_transactions.first().balance if financial_transactions else 0
    closing_financial_balance = financial_transactions.last().balance if financial_transactions else 0
    closing_balance = closing_financial_balance
    
    # Calculate opening and closing balance for bank transactions
    opening_bank_balance = bank_transactions.first().balance if bank_transactions else 0
    closing_bank_balance = bank_transactions.last().balance if bank_transactions else 0
    
    
    discrepancies = []
    matching_transactions = []
    
    
    # Simple reconciliation based on matching dates and amounts
    for banktransaction in bank_transactions:
        matching_records = financial_transactions.filter(date=banktransaction.date,debit=banktransaction.credit,credit=banktransaction.debit)
        if matching_records.exists():
            # Transaction found in both financial records and bank statement
            matching_transactions.append({
                'banktransaction': banktransaction,
                'financial_records': matching_records,
            })
        else:
            # Transaction only in bank statement, no match in financial records
            discrepancies.append({
                'type': 'Missing in Financial Records',
                'transaction': banktransaction,
            })
    # Check for financial records not present in the bank statement
    for financialtransaction in financial_transactions:
        matching_records=bank_transactions.filter(date=financialtransaction.date,debit=financialtransaction.credit,credit=financialtransaction.debit)
        
        if not matching_records.exists():
            # Transaction only in financial records, not in bank statement
            discrepancies.append({
                'type': 'Missing in Bank Statement',
                'financialtransaction':financialtransaction,
                
            })
    # Adjust opening and closing balances based on discrepancies
    for discrepancy in discrepancies:
        if discrepancy['type'] == 'Missing in Financial Records':
            # Deduct bank debit from opening balance and Add bank credit to opening balance of financial record
            closing_financial_balance  -= discrepancy['transaction'].debit or 0
            closing_financial_balance  += discrepancy['transaction'].credit or 0
        elif discrepancy['type'] == 'Missing in Bank Statement':
            closing_financial_balance  -= discrepancy['financialtransaction'].debit or 0
            closing_financial_balance  += discrepancy['financialtransaction'].credit or 0      
        
                 
    context = {
        'financial_transactions': financial_transactions,
        'bank_transactions': bank_transactions,
        'matching_transactions': matching_transactions,
        'discrepancies': discrepancies,
        'opening_bank_balance': opening_bank_balance,
        'closing_bank_balance': closing_bank_balance,
        'opening_financial_balance': opening_financial_balance,
        'closing_financial_balance': closing_financial_balance,
        'closing_balance': closing_balance,
        'show_reconciliation' : show_reconciliation,
    }    
    return render(request, 'reconcile.html', context)


@login_required
def voucher(request):
    vouch = Voucher.objects.all()
    if request.method == 'POST':
        voucher_type_to_filter = request.POST.get('voucher', '')
        PaymentVoucher = Voucher.objects.filter(name=voucher_type_to_filter)
        return render(request, 'voucher.html', {'PaymentVoucher': PaymentVoucher, 'selected_voucher': voucher_type_to_filter, 'vouch': vouch})

    # Handle the case when the form is not submitted (initial load)
    return render(request, 'voucher.html')


@login_required
def Account_Master(request):
    accounts = Account.objects.all()
    
    # Separate accounts into current and non-current categories
    current_assets = accounts.filter(account_type='Asset', account_subtype='Current')
    non_current_assets = accounts.filter(account_type='Asset', account_subtype='NonCurrent')
    
    # Separate Liabilities into current and non-current categories
    current_liabilities = accounts.filter(account_type='Liability', account_subtype='Current')
    non_current_liabilities = accounts.filter(account_type='Liability', account_subtype='NonCurrent')
    # taking equity 
    equity = accounts.filter(account_type='Equity')
    
    
    
    # Calculate total for each section
    total_current_assets = sum(account.amount for account in current_assets)
    total_non_current_assets = sum(account.amount for account in non_current_assets)

    total_current_liabilities = sum(account.amount for account in current_liabilities)
    total_non_current_liabilities = sum(account.amount for account in non_current_liabilities)

    total_equity = sum(account.amount for account in equity)
    
    # Calculate total assets and total liabilities + equity
    total_assets = total_current_assets + total_non_current_assets
    total_liabilities_equity = total_current_liabilities + total_non_current_liabilities + total_equity

     # Pass the data to the template
    context = {
        'current_assets': current_assets,
        'non_current_assets': non_current_assets,
        'total_current_assets': total_current_assets,
        'total_non_current_assets': total_non_current_assets,
        'current_liabilities': current_liabilities,
        'non_current_liabilities': non_current_liabilities,
        'total_current_liabilities': total_current_liabilities,
        'total_non_current_liabilities': total_non_current_liabilities,
        'equity': equity,
        'total_equity': total_equity,
        'total_assets': total_assets,
        'total_liabilities_equity': total_liabilities_equity,
    }

    return render(request, 'account.html', context)


