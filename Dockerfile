FROM python:3.8-alpine

RUN mkdir /code

COPY requirements.txt /code/

RUN pip install -r /code/requirements.txt

COPY app.py /code/

EXPOSE 5000

CMD ["python", "/code/app.py"]
