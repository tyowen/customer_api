from rest_framework.viewsets import ModelViewSet
from .models import Customer, CustomerSerializer

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer