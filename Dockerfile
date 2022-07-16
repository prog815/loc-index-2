FROM python:3.8-alpine

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

RUN python ./init_db.py

ENTRYPOINT ["python"]

CMD ["app.py"]