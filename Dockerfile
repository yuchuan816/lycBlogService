FROM python:3.7

MAINTAINER liuyuchuan liuyuchuan816@163.com

ENV DJANGO_SETTINGS_MODULE=lycBlogService.settings.prod

COPY . /server

WORKDIR /server

RUN pip install uwsgi uwsgitop mysql-connector-python -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN pip install -r ./requirements/prod.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 80

CMD uwsgi --ini uwsgi/uwsgi.ini
