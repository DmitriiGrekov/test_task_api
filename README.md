# Test task: Multi-level comment system 

This project is a solution to a test task.

## Preparation 

You will install Docker and docker-compose (https://docs.docker.com/compose/install/)

## Build your new env.

### Get the code from git.
```
git clone https://github.com/DmitriiGrekov/test_task_api
cd test_task_api 
```

### Build the base images
```
docker-compose build
```

### Migrate databases and  create django superuser 
```
docker-compose run web python manage.py migrate 
docker-compose run web python manage.py createsuperuser
```

If you want to change the database login data, change the settings in `test_task_api/blog/settings.py`, Replace the current DATABASES with
```
DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql_psycopg2",
        "NAME": "django_db",
        'USER': "admin",
        "PASSWORD": "admin",
        "HOST": "db",
    }
}

```

And modify `docker-compose.yml`

```
environment:
    POSTGRES_USER: admin
    POSTGRES_PASSWORD: admin
    POSTGRES_DB: django_db
```


### Starting the project
```
docker-compose up -d
```
You can now  visit http://localhost:8000


## Authors

* [Dmitrii Grekov] (https://github.com/DmitriiGrekov)

