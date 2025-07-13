Endpoint-Method	
/api/register/	POST	Register new user	Public
/api/login/	POST	Login user	Public
/api/logout/	POST	Logout user	Authenticated
/api/products/	GET	List all products	Public
/api/products/	POST	Create new product	Admin
/api/products/<id>/	GET	Get product details	Public
/api/products/<id>/	PUT/PATCH	Update product	Admin
/api/products/<id>/	DELETE	Delete product	Admin
/api/products/<id>/reviews/	GET	List product reviews	Public
/api/products/<id>/reviews/	POST	Create new review	Authenticated
/api/user/reviews/	GET	List user's reviews	Authenticated


Setup Instructions

Prerequisites
Python 3.8+
Django 4.0+
Django REST Framework

Installation
git clone https://github.com/Johhannn/pfactorial_.git
cd product-review-system


python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install djangorestframework

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
