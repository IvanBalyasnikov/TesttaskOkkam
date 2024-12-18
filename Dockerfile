FROM --platform=linux/x86_64 node:20
FROM python:3.11.9-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x ./start-app.sh
RUN chmod +x ./wait-for-it.sh

CMD ["bash" , "./start-app.sh"]