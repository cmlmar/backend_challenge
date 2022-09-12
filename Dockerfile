FROM python:3.10.7-slim-buster

COPY . /src

RUN pip install -r /src/requirements.txt

ENTRYPOINT ["python"]

CMD ["/src/main.py"]