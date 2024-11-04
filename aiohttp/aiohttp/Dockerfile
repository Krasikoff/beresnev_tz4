FROM library/python:3.10-slim

COPY requirements.txt /app/
COPY main.py /app/

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD [ "python", "main.py" ]
