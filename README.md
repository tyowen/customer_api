# Customer API

This is a simple RESTful API that manages customers.

## Design

The API is designed using the following technologies:

- Django: Given the time constraints, Django was chosen as the web framework for the API as it provides a lot of built-in functionality that would otherwise have to be implemented from scratch or with additional libraries. 
- Django Rest Framework: This library was used to create the API endpoints and serialize the data.
- PostgreSQL: The database used to store the customer data.

## Development

### Start the API
`python src/manage.py runserver`

## Dev Notes:

- To keep the workflow simple, commits are made directly to the main branch. In real-world scenarios, feature branches would be created and merged into the main branch via pull requests.