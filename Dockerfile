FROM python:3.9

WORKDIR /app
RUN apt install -y git

RUN git clone https://github.com/Bliss-e-V/bosch-hackathon-24

WORKDIR /app/bosch-hackathon-24

RUN pip install -r requirements.txt

COPY .env .env

CMD ["python", "-m",  "flask",  "--app", "src/server",  "run",  "--host=0.0.0.0", "--port=80"] 

EXPOSE 80