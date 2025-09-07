FROM python:3.11-slim

RUN pip install --no-cache-dir openai==0.28.1

COPY entrypoint.py /entrypoint.py
RUN chmod +x /entrypoint.py

ENTRYPOINT ["python", "/entrypoint.py"]