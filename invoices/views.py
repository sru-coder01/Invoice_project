from rest_framework import viewsets
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    http_method_names = ['get', 'post', 'put', 'delete']  # Allow PUT and DELETE methods


class InvoiceDetailViewSet(viewsets.ModelViewSet):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer
    http_method_names = ['get', 'post', 'put', 'delete']  # Allow PUT and DELETE methods
