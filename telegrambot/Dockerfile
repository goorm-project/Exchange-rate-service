FROM python:3.9-slim AS builder
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

FROM python:3.9.6-slim-buster
COPY --from=builder  /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
ADD init_db.py init_db.py
ADD update_db.py update_db.py
ADD db_readwrite.py db_readwrite.py
ADD test.py .
CMD ["python", "test.py"]