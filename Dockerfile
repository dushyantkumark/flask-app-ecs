FROM python:3.7
RUN apt-get update -y 
WORKDIR /app
COPY ./ /app
RUN pip install flask
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]