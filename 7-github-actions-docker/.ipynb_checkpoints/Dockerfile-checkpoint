FROM python:3.6-slim
COPY ./app.py /deploy/
COPY ./requirements.txt /deploy/
COPY ./iris-model.model /deploy/
WORKDIR /deploy/
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python", "app.py"]
