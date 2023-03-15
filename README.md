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
    'rest_framework',
    'celery',
    'django_celery_results',
    'django_celery_beat',
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



## Celery Beat

<p> Using Celery Beat in django for sending the earnings report to the finance department regarding every day at 4 p.m </p>

* Created the file Celery.py inside pricing module where we have the settings.py of the project
* Created the file Tasks.py to write a task that to be perform inside the celery in price app
* Add celery app inside __init__.py file 
* Connect to the smtp server for sending the email  and have a secure connection



<p> To schedule the email task on load of url we can run the worker command of celery.

~~~tex
celery -A pricing_module worker -l info
~~~



To schedule the email task everyday we can add our scheduler using Beat in celery.py file

```python
app.conf.beat_schedule = {
    'send-mail-every-day-at-4pm': {
        'task': 'price.tasks.send_email_task',
        'schedule': crontab(hour=16, minute=0),
    }
}
```

 for this to make execute we run the beat command of celery.

~~~ 
celery -A pricing_module beat -l info
~~~

This will scheduler the task to send the mail every day at 4 pm.
