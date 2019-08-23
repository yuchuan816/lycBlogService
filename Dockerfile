FROM python:3.7

MAINTAINER liuyuchuan liuyuchuan816@163.com

COPY . /server

WORKDIR /server

RUN pip install uwsgi uwsgitop -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN pip install -r ./requirements/prod.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 8000

CMD ["uwsgi", "--ini", "uwsgi.ini"]
