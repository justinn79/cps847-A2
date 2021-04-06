FROM python:3.6.1
WORKDIR /cps847-A2
ADD . /cps847-A2
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","web_application.py"]
