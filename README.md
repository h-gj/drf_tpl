# A RESTFul API Template Built with Django & DRF.


### Following features implemented

- Custom renderer for modern response structure
```javascript
{
    "code": 10000,
    "messsage": "success",
    "data": {}
}
```

- Custom exception handler
```javascript
{
    "code": 50000,
    "message": "division by zero",
    "data": null
}
```

- Friendly validation error
```javascript
{
    "code": 40000,
    "message": "username is required.password is required.",
    "data": null
}
```

- Cache integrated

Cache response with the help of django signals and drf-extensions caching


### Startup
#### Install dependencies
> ```pip install -r requirements.txt```

#### Config local settings
> ```cd drf_tpl```

Create a new file `settings_local.py`, paste following config into it and replace `***` with your own real config. You could even replace database engine depending on your situation:
```Python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '***',
        'USER': '***',
        'PASSWORD': '***',
        'HOST': '***',
    }
}
```
#### Have fun
> python manage.py runserver