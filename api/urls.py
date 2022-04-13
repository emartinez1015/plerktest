from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .viewsets import PlerkReportView, CompanyViewSet, TransactionSummaryView


router = DefaultRouter()
router.register(r'report/summary', PlerkReportView, basename='summary')
router.register(r'report/company', CompanyViewSet, basename='company-report')
router.register(r'report/transaction-sumary', TransactionSummaryView, basename='company-pro')



urlpatterns = [
    path('', include(router.urls))
]