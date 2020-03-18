FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get install vim mariadb-client dnsutils net-tools nmap -y
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./ /code/
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8004"]
