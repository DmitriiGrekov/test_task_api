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

_If you have a mistake_ ___Is the server running on host "db" (192.168.80.2) and accepting TCP/IP connections on port 5432?___ _replace the line in_ `docker-compose.yml`

```
ports:
    - "54321:5432"
```

On

```
ports:
    - "5432:5432"

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

_If you have a mistake_ ___Error starting userland proxy: listen tcp4 0.0.0.0:5432: bind: address already in use___ _replace the line in_ `docker-compose.yml`

```
ports:
    - "5432:5432"
```

On

```
ports:
    - "54321:5432"

```


You can now  visit http://localhost:8000


### API Documentation

To get a list of posts, you need to send a GET request to

`http://127.0.0.1:8000/api/posts/`

Response

```
{
    "id": 2,
    "title": "Second post",
    "content": "The best",
    "created": "2022-04-13T15:08:11.674949Z",
    "author": 1,
    "comments": [
        {
            "id": 1,
            "post": 2,
            "author_name": "Dmitrii",
            "text": "Hello",
            "pub_date": "2022-04-13T15:08:42.686716Z",
            "level": 0,
            "children": [
                {
                    "id": 2,
                    "post": 2,
                    "author_name": "Dmitrii",
                    "text": "Hello",
                    "pub_date": "2022-04-13T15:08:57.432641Z",
                    "level": 1,
                    "children": []
                }
            ]
        }
    ]
}
```

To view a separate post, you need to send a GET request to `http://127.0.0.1:8000/api/post/{post_id}`



To add a post to the database, you need to send a POST request to `http://127.0.0.1:8000/api/posts/`

with these fields


```
{
    "title": "Title",
    "content": "content",
    "author": User_Id,
    "comments": []
}

```

Response

```
{
    "id": 2,
    "title": "asdf",
    "content": "asdf",
    "created": "2022-04-13T16:13:53.915037Z",
    "author": 1,
    "comments": []
}

```

To add comments of the first level, you need to send a POST request to `http://127.0.0.1:8000/api/comments/add/{post_id}/` 
with these fields

```
{
    "author_name": "Name",
    "text": "Text"
}

```

Response


```
{
    "author_name": "Name",
    "text": "Text"
}
```

To add top-level comments, you need to send a POST request to `http://127.0.0.1:8000/api/comments/add/{post_id}/`
with these fields

```
{
    "author_name": "Name",
    "text": "Text",
    "parent_id": Parent_ID 
}

```
Where the parent_id is the id of the parent comment

## Authors

* [Dmitrii Grekov] (https://github.com/DmitriiGrekov)

