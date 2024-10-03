# Django REST API for Book Management

This project demonstrates a simple RESTful API built with Django and Django REST Framework. 
It is designed for educational purposes to showcase skills in building APIs using Django.

## Purpose

This repository showcases:

- **Creating a REST API**: Demonstrating how to set up API endpoints with Django REST Framework.
- **Model-View-Serializer Workflow**: Implementing the MVC architecture using Django Models, Views, and DRF Serializers.
- **Basic CRUD Operations**: The project implements basic operations to retrieve and add book records.

## API Endpoints

### 1. List of Books (GET `/api/`)

This endpoint retrieves all books from the database.

- **Method**: GET
- **URL**: `/api/`
- **Response Example**: 
  ```json
  [
      {
          "id": 1,
          "name": "Django for Beginners",
          "author": "William S. Vincent",
          "created_dt": "2023-01-01T12:00:00Z"
      },
      {
          "id": 2,
          "name": "Two Scoops of Django",
          "author": "Daniel Roy Greenfeld",
          "created_dt": "2023-02-01T12:00:00Z"
      }
  ]

  ### 2. Add a New Book (POST `/api/add`)

This endpoint allows users to add a new book to the database.

- **Method**: POST
- **URL**: `/api/add`

#### Request Body Example:

```json
{
    "name": "Two Scoops of Django",
    "author": "Daniel Roy Greenfeld"
}

### Logos

![Python Logo](https://www.python.org/community/logos/python-logo.png)
![Django Logo](https://www.djangoproject.com/m/img/logos/django-logo-negative.svg)
![DRF Logo](https://www.django-rest-framework.org/img/logo.png)
