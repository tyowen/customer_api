import click
import requests
from tabulate import tabulate

API_BASE_URL = "http://localhost:8000/api"


class CustomerClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def list_customers(self):
        response = requests.get(f"{self.base_url}/customers/")
        response.raise_for_status()
        return response.json()

    def get_customer(self, customer_id: str):
        response = requests.get(f"{self.base_url}/customers/{customer_id}/")
        response.raise_for_status()
        return response.json()

    def create_customer(self, data: dict):
        response = requests.post(f"{self.base_url}/customers/", json=data)
        response.raise_for_status()
        return response.json()

    def update_customer(self, customer_id: str, data: dict):
        response = requests.put(f"{self.base_url}/customers/{customer_id}/", json=data)
        response.raise_for_status()
        return response.json()

    def delete_customer(self, customer_id: str):
        response = requests.delete(f"{self.base_url}/customers/{customer_id}/")
        response.raise_for_status()
        return None


@click.group()
def cli():
    """Customer API CLI"""
    pass


def display_customers(customers):
    headers = ["ID", "First Name", "Last Name", "Email", "Phone"]
    rows = [
        [c["id"], c["first_name"], c["last_name"], c["email"], c["phone_number"]]
        for c in customers
    ]
    click.echo(tabulate(rows, headers=headers, tablefmt="grid"))


@cli.command()
def list():
    """List all customers"""
    client = CustomerClient(API_BASE_URL)
    customers = client.list_customers()
    display_customers(customers)


@cli.command()
@click.argument("customer_id")
def get(customer_id):
    """Get a specific customer"""
    client = CustomerClient(API_BASE_URL)
    customer = client.get_customer(customer_id)
    display_customers([customer])



@cli.command()
@click.argument("first_name")
@click.argument("last_name")
@click.argument("email")
@click.argument("phone_number")
def create(first_name, last_name, email, phone_number):
    """Create a new customer"""
    client = CustomerClient(API_BASE_URL)
    data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone_number": phone_number,
    }
    customer = client.create_customer(data)
    click.echo(click.style(f"Customer created with ID: {customer['id']}", fg="green"))
    display_customers([customer])


@cli.command()
@click.argument("customer_id")
@click.argument("first_name")
@click.argument("last_name")
@click.argument("email")
@click.argument("phone_number")
def update(customer_id, first_name, last_name, email, phone_number):
    """Update an existing customer"""
    client = CustomerClient(API_BASE_URL)
    data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone_number": phone_number,
    }
    customer = client.update_customer(customer_id, data)
    click.echo(click.style(f"Customer with ID: {customer_id} updated", fg="green"))
    display_customers([customer])


@cli.command()
@click.argument("customer_id")
def delete(customer_id):
    """Delete a customer"""
    client = CustomerClient(API_BASE_URL)
    client.delete_customer(customer_id)
    click.echo(click.style(f"Customer with ID: {customer_id} deleted", fg="green"))


if __name__ == "__main__":
    cli()
