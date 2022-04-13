from django.db import models
from .data import TRANSACTION_STATUS
from plerktest.utils.models import PlerkModel
from apps.users.models import User
from apps.transactions.managers import TransactionManager

class Company(PlerkModel):
    name = models.CharField(max_length=250)
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Transaction(PlerkModel):
    company = models.ForeignKey(Company, verbose_name="Company", on_delete=models.PROTECT)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(verbose_name="Transaction date")
    status_transaction = models.CharField(max_length=50, choices=TRANSACTION_STATUS)
    status_approved = models.BooleanField()
    objects = TransactionManager()

    def __str__(self):
        return f"{self.company} - {self.price}"