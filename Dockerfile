FROM python:3.7

MAINTAINER liuyuchuan liuyuchuan816@163.com

ENV DJANGO_SETTINGS_MODULE=lycBlogService.settings.prod

COPY . /server

WORKDIR /server

RUN pip install -r ./requirements/prod.txt

EXPOSE 80

# CMD python manage.py migrate && uwsgi --ini uwsgi/uwsgi.ini
CMD uwsgi --ini uwsgi/uwsgi.ini
