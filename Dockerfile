FROM python:3.7

MAINTAINER liuyuchuan liuyuchuan816@163.com

COPY . /server

WORKDIR /server

RUN pip install uwsgi uwsgitop

RUN pip install -r ./requirements/prod.txt

EXPOSE 8000

#ENTRYPOINT ["python"]

#CMD ["manage.py", "runserver", "0.0.0.0:8000"]

CMD ["uwsgi", "--ini", "django_uwsgi.ini"]
