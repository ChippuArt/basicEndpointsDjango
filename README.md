```markdown
# Django RESTful API Project

This project is a demonstration of building RESTful APIs using Django and Django REST Framework (DRF). It showcases how to implement CRUD operations and utilize Django's powerful queryset features for searching and filtering data.

## Features

- RESTful API architecture using Django REST Framework.
- CRUD operations on models via RESTful endpoints.
- Advanced data querying and filtering with Django querysets.
- Use of dynamic URL query parameters for data filtering.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6+
- Django 3.1+
- Django REST Framework

### Installing

First, clone the repository to your local machine:

```bash
git clone https://github.com/ChippuArt/basicEndpointsDjango.git
```

Navigate to the project directory:

```bash
cd basicEndpointsDjango
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run migrations to create the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Now, you can access the API at `http://127.0.0.1:8000/api/`.
Three APIs exists for testings purposes: articles, posts, blogs.


## Usage

Here's how to use the APIs with examples:

### List Posts

GET `/api/posts/`

### Create a Post

POST `/api/posts/`

```json
{
  "title": "Sample Post",
  "content": "This is a sample post.",
  "author": "AuthorName"
}
```

### Update a Post

PUT `/api/posts/<id>/`

```json
{
  "title": "Updated Title",
  "content": "Updated content."
}
```

### Delete a Post

DELETE `/api/posts/<id>/`

## Authors

- ChippuArt - *Initial work* - [ChippuArt(https://github.com/ChippuArt)](https://github.com/ChippuArt/basicEndpointsDjango/new/main?filename=README.md)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
