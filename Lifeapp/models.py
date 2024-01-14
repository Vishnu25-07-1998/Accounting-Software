from django.db import models

# Create your models here.

class FinancialRecord(models.Model):
    date = models.DateField()
    particulars = models.CharField(max_length=255)
    debit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    credit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.date
    

class BankStatement(models.Model):
    date = models.DateField()
    particulars = models.CharField(max_length=255)
    debit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    credit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.date
    
class Expense(models.Model):
    date = models.DateField()
    expense_type = models.CharField(max_length=255)
    vendor_description = models.CharField(max_length=255)
    amount = models.IntegerField()
    balance = models.IntegerField()

    def __str__(self):
        return f"{self.date} - {self.expense_type} - {self.vendor_description}"
    
    
class AccountRecievable(models.Model):
    vendor_id = models.CharField(max_length=10, unique=True)
    invoice_date = models.DateField()
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    balance = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.vendor_id} - {self.invoice_date} - {self.due_date}"
    
    
class PatientLedger(models.Model):
    patient_id = models.CharField(max_length=10, unique=True)
    patient_name = models.CharField(max_length=50)
    admission_date = models.DateField()
    discharge_date = models.DateField()
    total_charges = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.patient_id} - {self.patient_name}"
    
    
class Voucher(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    pay = models.CharField(max_length=50)
    auth = models.CharField(max_length=50)
    approve = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name} - {self.desc}"
    
class Account(models.Model):
    ACCOUNT_TYPES = [
        ('Asset', 'Asset'),
        ('Liability', 'Liability'),
        ('Equity', 'Equity'),
    ]
    ACCOUNT_SUBTYPES = [
        ('Current', 'Current'),
        ('NonCurrent', 'Non-Current'),
    ]

    name = models.CharField(max_length=255)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    account_subtype = models.CharField(max_length=10, choices=ACCOUNT_SUBTYPES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.account_type}"
    
    
class GeneralLedger(models.Model):
    Date = models.DateField()
    Account = models.CharField(max_length=255)
    Debit = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    Credit = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.Account} - {self.Date}"