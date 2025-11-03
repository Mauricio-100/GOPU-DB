FROM python:3.11

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y postgresql
RUN pip install --no-cache-dir -r requirements.txt

# Configuration PostgreSQL codée en dur
ENV POSTGRES_DB=gopu
ENV POSTGRES_USER=ceose
ENV POSTGRES_PASSWORD=agentic
ENV POSTGRES_HOST=localhost
ENV POSTGRES_PORT=5432

EXPOSE 8080
CMD ["python", "app.py"]
