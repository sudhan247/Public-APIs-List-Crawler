FROM python:3.8
WORKDIR /new
COPY ./postman.py /new
RUN pip install requests
RUN pip install pandas 
RUN pip install sqlalchemy 
RUN pip install cx_oracle
RUN pip install psycopg2
