from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Invoice

class InvoiceAPITest(TestCase):

    def setUp(self):
        self.invoice = Invoice.objects.create(Date="2024-01-08", InvoiceCustomerName="Customer")

    def test_get_invoices(self):
        url = reverse('invoices:invoice-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invoice(self):
        url = reverse('invoices:invoice-list')
        data = {"Date": "2024-01-08", "InvoiceCustomerName": "Customer"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_invoice_detail(self):
        url = reverse('invoices:invoice-detail', args=[self.invoice.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invoice(self):
        url = reverse('invoices:invoice-detail', args=[self.invoice.id])
        data = {"Date": "2024-01-09", "InvoiceCustomerName": "Updated Customer"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_invoice(self):
        url = reverse('invoices:invoice-detail', args=[self.invoice.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
