FROM python:3.8-slim-buster

WORKDIR ./ .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python3"]
CMD ["init_db.py"]
CMD ["main.py"]