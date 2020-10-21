FROM python:3.8.6-slim


RUN apt-get update && apt-get install -y gcc python3-dev
COPY . .
RUN pip3 install --no-cache-dir -I -r requirments.txt

CMD ["python3", "main.py"]