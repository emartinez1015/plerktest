from django.db.models import Count
from rest_framework import serializers
from apps.transactions.models import Company


class CompanyReportSerializer(serializers.ModelSerializer):
    transaction_charged = serializers.SerializerMethodField()
    transaction_not_charged = serializers.SerializerMethodField()
    most_transactions_day = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ("name", "transaction_charged", "transaction_not_charged", "most_transactions_day")
    
    def get_transaction_charged(self, obj):
        return obj.transaction_set.charges().count()
    
    def get_transaction_not_charged(self, obj):
        return obj.transaction_set.not_charges().count()

    def get_most_transactions_day(self, obj):
        return obj.transaction_set.dates("date", "day").annotate(
            count=Count("id")).values("date__date", "count").order_by("-count").first().get("date__date")
    