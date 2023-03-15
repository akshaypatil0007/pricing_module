# pricing_module
This repository contents the Django code for calculating the price for billing service

## Requirements

```
Python 3.7+
Django==4.1.7
djangorestframework==3.14.0
```

## Installation

```
pip3 install -r requirement.txt
```

### Build Django Project

```
python3 -m django startproject pricing_module
python3 manage.py startapp price
```



## Example

### Create Superuser for Django Admin

#### Command

```python
python3 manage.py createsuperuser
```

#### Credential

```tex
price
price@gmail.com
price
```

## Code Description

##### pricing_module/settings.py

~~~
After creating the app we have to add the name in settings.py inside INSTALLED_APP if we dont add we can unable to make the migration for the models.
~~~

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'price',
    'rest_framework'
]
```

##### price/urls.py

~~~
Creating file new urls.py inside the app price
~~~

```python
from django.urls import path
from .views import UserList,UserDetails
urlpatterns = [
    path('user/', UserList.as_view()),
    path('user/<int:id>', UserDetails.as_view()),
]
```



##### price/models.py

```
Here we build the structure for creating the database inside sqlite db
```

```
Then after creating the models we have to make migration for the models. This will create the file 0001_initial.py inside app/migration folder to check the query that it will run into the sql db.
```

~~~ 
$ python3 manage.py makemigrations
~~~

```
Then after the migration we have to migrate the project for implement and create the table inside the mysql db
```

```
$ python3 manage.py migrate
```

### Run it

Run the server with:


```console
$ python3 manage.py runserver 127.0.0.1:8000
```

### Check it

Open your browser at <a href="http://127.0.0.1:8000/items/5?q=somequery" class="external-link" target="_blank">http://127.0.0.1:8000/admin/ </a>

> To open the django admin panel 
>
> * username - price
> * password - price

Open your browser at <a href="http://127.0.0.1:8000/items/5?q=somequery" class="external-link" target="_blank">http://127.0.0.1:8000/user/ </a>

> To open the list of all user and add new user

Open your browser at <a href="http://127.0.0.1:8000/items/5?q=somequery" class="external-link" target="_blank">http://127.0.0.1:8000/user/10 </a>

> To open the specific user list with the modification and deletion of user
>




