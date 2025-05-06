FROM python:3.10-slim-buster
EXPOSE 5000
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir --timeout=1000
COPY ./*.py ./
COPY ./news_dataset ./news_dataset
ENTRYPOINT [ "python", "main.py", "-P", "5000", "-H", "0.0.0.0"]