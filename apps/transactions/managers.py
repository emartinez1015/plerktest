from django.db import models
from apps.transactions.data import TRANSACTION_CLOSED, CONVERSION_FACTOR
from django.db.models.functions import Concat, Cast
    

class TransactionManager(models.Manager):
    
    def charges(self):
        return self.get_queryset().filter(status_approved=True, status_transaction=TRANSACTION_CLOSED)
    
    def not_charges(self):
        return self.get_queryset().filter(status_approved=False, status_transaction=TRANSACTION_CLOSED)
    
    def sales(self):
        return self.charges() \
            .values("company__name").annotate(total=models.Sum("price"))
    
    def most_sales_company(self):
        return self \
            .sales().order_by("-total").first().get("company__name")

    def lowest_sales_company(self):
        return self \
            .sales().order_by("total").first().get("company__name")

    def transaction_charged(self):
        return self \
            .charges().aggregate(total=models.Sum("price")).get("total") / CONVERSION_FACTOR

    def transaction_not_charged(self): 
        return self \
            .not_charges().aggregate(total=models.Sum("price")).get("total") / CONVERSION_FACTOR

    def most_sales_rejected_company(self):
        return self \
            .not_charges().values("company__name").annotate(count=models.Count("price")) \
            .order_by("-count").first().get("company__name")
        
    def by_month_date_range(self, date_initial, date_final):
        return self \
            .charges().filter(date__date__range=[str(date_initial), str(date_final)]) \
            .dates("date", "month") \
            .annotate(
                count=models.Count("id"),
                total=models.Sum(models.F("price") / CONVERSION_FACTOR),
                year_month=Concat(
                    Cast(
                        'date__year', 
                        models.CharField()), models.Value('-'), 
                        Cast('date__month', models.CharField()
                    )
                ),
            ) \
            .values("date__year","date__month","year_month","count","total")
        