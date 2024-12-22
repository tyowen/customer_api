import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from .models import Customer


@pytest.mark.django_db
class TestCustomerAPI:
    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def customer_data(self):
        return {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone_number": "+1234567890",
        }

    def test_create_customer(self, api_client, customer_data):
        url = reverse("customer-list")
        response = api_client.post(url, customer_data, format="json")
        assert response.status_code == 201
        assert response.data["first_name"] == customer_data["first_name"]
        assert response.data["last_name"] == customer_data["last_name"]
        assert response.data["email"] == customer_data["email"]
        assert response.data["phone_number"] == customer_data["phone_number"]

    def test_get_customer(self, api_client, customer_data):
        customer = Customer.objects.create(**customer_data)
        url = reverse("customer-detail", kwargs={"pk": customer.id})
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.data["first_name"] == customer_data["first_name"]
        assert response.data["last_name"] == customer_data["last_name"]
        assert response.data["email"] == customer_data["email"]
        assert response.data["phone_number"] == customer_data["phone_number"]

    def test_update_customer(self, api_client, customer_data):
        customer = Customer.objects.create(**customer_data)
        url = reverse("customer-detail", kwargs={"pk": customer.id})
        updated_data = customer_data.copy()
        updated_data["first_name"] = "Jane"
        response = api_client.put(url, updated_data, format="json")
        assert response.status_code == 200
        assert response.data["first_name"] == "Jane"
        assert response.data["last_name"] == customer_data["last_name"]
        assert response.data["email"] == customer_data["email"]
        assert response.data["phone_number"] == customer_data["phone_number"]

    def test_get_customers(self, api_client):
        Customer.objects.create(
            first_name="FA", last_name="LA", email="fa.la@example.com"
        )
        Customer.objects.create(
            first_name="FB", last_name="LB", email="fb.lb@example.com"
        )
        url = reverse("customer-list")
        response = api_client.get(url)
        assert response.status_code == 200
        assert len(response.data) == 2

    def test_dup_email(self, api_client, customer_data):
        Customer.objects.create(**customer_data)
        url = reverse("customer-list")
        response = api_client.post(url, customer_data, format="json")
        assert response.status_code == 400
        assert "email" in response.data
        assert response.data["email"][0].code == "unique"

    def test_missing_attr(self, api_client, customer_data):
        del customer_data["first_name"]
        url = reverse("customer-list")
        response = api_client.post(url, customer_data, format="json")
        assert response.status_code == 400
        assert "first_name" in response.data
        assert response.data["first_name"][0].code == "required"
