FROM python:3.11-alpine AS stage
WORKDIR app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY main.py /app/main.py

FROM stage AS test
RUN pip install pytest trio
COPY test_main.py /app/test_main.py
ENTRYPOINT ["pytest"]

FROM stage AS prod
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]



#FROM BUILDER AS PROD
#ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--log-config", "config/log_config.yaml"]
#ENTRYPOINT ["python", "-m", "main.py"]
#CMD ["pip", "install", "-r", "requirements.txt"]


#RUN pip install






