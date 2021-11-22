FROM python:3.9-slim AS builder
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

FROM python:3.9.6-slim-buster
RUN ln -snf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
COPY --from=builder  /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
ADD db_readwrite.py db_readwrite.py
ADD main.py .
CMD ["python", "main.py"]