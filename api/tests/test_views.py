from rest_framework.test import APITestCase
from django.shortcuts import reverse
from apps.users.models import User
from apps.transactions.models import Company


class TestReportViews(APITestCase):
    fixtures = [
        "users.yaml",
        "companies.yaml",
        "transactions.yaml"
    ]
    def setUp(self):
        self.user = User.objects.first()
        self.company = Company.objects.first()
        self.client.force_authenticate(user=self.user)
        
    def test_summary_report_not_authenticated(self):
        self.client.logout()
        self.assertEqual(self.client.get(reverse("api:summary-list")).status_code, 401)

    def test_summary_report_authenticated(self):
        self.assertEqual(self.client.get(reverse("api:summary-list")).status_code, 200)

    def test_company_report_not_authenticated(self):
        self.client.logout()
        self.assertEqual(self.client.get(reverse("api:company-report-detail", kwargs={"pk": str(self.company.id)})).status_code, 401)

    def test_company_report_authenticated(self):
        self.assertEqual(self.client.get(reverse("api:company-report-detail", kwargs={"pk": str(self.company.id)})).status_code, 200)    

    def test_transaction_summary_report_not_authenticated(self):
        self.client.logout()
        ini_date = "2021-01"
        fin_date = "2021-03"
        path = reverse("api:company-pro-list")
        result = '%s?ini_date=%s&fin_date=%s' % (path, ini_date, fin_date)
        self.assertEqual(self.client.get(result).status_code, 401)

    def test_transaction_summary_report_authenticated(self):
        ranges_dates = { 'ini_date': "2021-01" , "fin_date": "2021-03"}
        ini_date = "2021-01"
        fin_date = "2021-03"
        path = reverse("api:company-pro-list")
        result = '%s?ini_date=%s&fin_date=%s' % (path, ini_date, fin_date)
        self.assertEqual(self.client.get(result).status_code, 200)
