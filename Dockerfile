FROM python:3.7

MAINTAINER liuyuchuan <liuyuchuan816@163.com>

COPY . /app

WORKDIR /app

RUN pip install -r ./requirements/prod.txt

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["manage.py", "runserver", "5000"]