import csv
from django.core.management.base import BaseCommand
from Lifeapp.models import FinancialRecord, BankStatement,  PatientLedger, Expense, AccountRecievable, Account, Voucher,GeneralLedger

class Command(BaseCommand):
    help = 'Load data from CSV files into Django models'

    def handle(self, *args, **options):
        #Specify the paths to your CSV files
        financial_record_file = 'static/CSV_FILES/financial_record.csv'
        bank_statement_file = 'static/CSV_FILES/bank_statement.csv'
        Patient_ledger_file = 'static/CSV_FILES/Patient_Ledger.csv'
        Expense_ledger_file = 'static/CSV_FILES/Expense_Ledger.csv'
        AccountRecievable_ledger_file = 'static/CSV_FILES/Account_Recievable_Ledger.csv'
        Account_Master = 'static/CSV_FILES/master.csv'
        Voucher_file = 'static/CSV_FILES/voucher.csv'
        General_ledger = 'static/CSV_FILES/General_ledger.csv'
        
        
        with open(General_ledger, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                GeneralLedger.objects.create(
                    Date=row['Date'],
                    Account=row['Account'],
                    Debit=row['Debit'] if row['Debit'] else None,
                    Credit=row['Credit'] if row['Credit'] else None,
                )
                
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))

        #Load data into FinancialRecord model
        with open(financial_record_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                FinancialRecord.objects.create(
                    date=row['DATE'],
                    particulars=row['PARTICULARS'],
                    debit=row['DEBIT'] if row['DEBIT'] else None,
                    credit=row['CREDIT'] if row['CREDIT'] else None,
                    balance=row['BALANCE']
                )

        # Load data into BankStatement model
        with open(bank_statement_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                BankStatement.objects.create(
                    date=row['DATE'],
                    particulars=row['PARTICULARS'],
                    debit=row['DEBIT'] if row['DEBIT'] else None,
                    credit=row['CREDIT'] if row['CREDIT'] else None,
                    balance=row['BALANCE']
                )
        
        # Load data into Patient model
        with open(Patient_ledger_file, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                PatientLedger.objects.create(
                    patient_id=row['PatientID'],
                    patient_name=row['PatientName'],
                    admission_date=row['AdmissionDate'],
                    discharge_date=row['DischargeDate'],
                    total_charges=row['TotalCharges($)'],
                    balance=row['Balance']
               )
        # Load data into Expense model        
        with open(Expense_ledger_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Expense.objects.create(
                    date=row['Date'],
                    expense_type=row['ExpenseType'],
                    vendor_description=row['Vendor/Description'],
                    amount=row['Amount($)'],
                    balance=row['Balance']
                )
        # Load data into AccountRecievable model 
        with open(AccountRecievable_ledger_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                AccountRecievable.objects.create(
                    vendor_id=row['VendorID'],
                    invoice_date=row['InvoiceDate'],
                    due_date=row['DueDate'],
                    amount=row['Amount($)'],
                    balance=row['Balance']
                )
                
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
        
        #Load data into Account
        with open(Account_Master, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Account.objects.create(
                    name=row['name'],
                    account_type=row['account_type'],
                    account_subtype=row['account_subtype'] if 'account_subtype' in row else None,
                    amount=row['amount'],
                )
                
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
        
        
        
        
        # Load data into Voucher
        with open(Voucher_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Voucher.objects.create(
                    date=row['DATE'],
                    name=row['Name'],
                    desc=row['Description'],
                    amount=row['Amount'],
                    pay=row['Payment'],
                    auth=row['Authorize'],
                    approve=row['Approved'],
                )
                
                
        
 
