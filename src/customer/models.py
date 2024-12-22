from uuid import uuid4

from django.db.models import CharField, EmailField, Model, UUIDField
from rest_framework.serializers import ModelSerializer


class Customer(Model):
    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = CharField(max_length=100)
    middle_name = CharField(max_length=100, null=True, blank=True)
    last_name = CharField(max_length=100)
    email = EmailField(unique=True)
    phone_number = CharField(max_length=20, null=True, blank=True)


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
