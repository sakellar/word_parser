FROM python:2.7

EXPOSE 8888

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY src/ /app/src/
COPY templates/ /app/templates/
CMD python src/main_module.py
