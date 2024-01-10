from django.urls import path
from .views import InvoiceViewSet

app_name = 'invoices'

urlpatterns = [
    path('', InvoiceViewSet.as_view({'get': 'list', 'post': 'create'}), name='invoice-list'),
    path('<int:pk>/', InvoiceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='invoice-detail'),
    # Add other URL patterns as needed
]
