FROM python:3

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITECODE 1

WORKDIR /usr/src/test_api

COPY ./requirements.txt /usr/src

RUN pip install -r /usr/src/requirements.txt



COPY . /usr/src/test_api

COPY ./entrypoint.sh /usr/src
RUN chmod +x /usr/src/entrypoint.sh

EXPOSE 8000


CMD ["python", "manage.py", "initadmin"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
