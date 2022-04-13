from apps.transactions.models import Company
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, response, mixins
from .serializers import CompanyReportSerializer
from rest_framework.permissions import IsAuthenticated
from . import swager_config
from apps.transactions.models import Transaction
from datetime import datetime
import calendar
from rest_framework.serializers import ValidationError


class PlerkReportView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        data = self.get_report()
        return response.Response(data)

    def get_report(self):
        most_sales_company = Transaction.objects.most_sales_company()
        lowest_sales_company = Transaction.objects.lowest_sales_company()
        transaction_charged = Transaction.objects.transaction_charged()
        transaction_not_charged = Transaction.objects.transaction_not_charged()
        most_sales_rejected_company = Transaction.objects.most_sales_rejected_company()
        data = {
            "most_sales_company": most_sales_company,
            "lowest_sales_company": lowest_sales_company,
            "transaction_charged": transaction_charged,
            "transaction_not_charged": transaction_not_charged,
            "most_sales_rejected_company": most_sales_rejected_company,
        }
        return data

class CompanyViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CompanyReportSerializer
    queryset = Company.objects.all()


class TransactionSummaryView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
   
    @swagger_auto_schema(**swager_config.transaction_summary_list)
    def list(self, request):
        try:
            di = request.query_params.get('ini_date')
            df = request.query_params.get('fin_date')
            date_initial = datetime.strptime(di, "%Y-%m").date()
            date_final =  datetime.strptime(df, "%Y-%m")
            date_final = date_final.replace(day=calendar.monthrange(date_final.year, date_final.month)[1]).date()
            data = Transaction.objects.by_month_date_range(date_initial, date_final)
            return response.Response(data)
        except ValueError as e:
            raise ValidationError(str(e))
        