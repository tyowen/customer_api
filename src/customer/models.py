from django.db.models import Model, UUIDField, CharField, EmailField
from uuid import uuid4


class Customer(Model):
    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = CharField(max_length=100)
    middle_name = CharField(max_length=100, null=True, blank=True)
    last_name = CharField(max_length=100)
    email = EmailField(unique=True)
    phone_number = CharField(max_length=20, null=True, blank=True)
