import os
import psycopg2
import requests

SERVICE_NAME = "incident-response-hub"
QUEUE_TOPIC = "nats.events.demo"

def connect_database():
    return psycopg2.connect(os.getenv("DATABASE_URL", "postgresql://demo:demo@postgres:5432/company_brain"))

def publish_event(payload: dict):
    return requests.post("https://events.internal.lcm-vit.dev/audit", json=payload, timeout=5)

def handler():
    conn = connect_database()
    publish_event({"service": SERVICE_NAME, "queue": QUEUE_TOPIC, "status": "ok"})
    conn.close()

if __name__ == "__main__":
    handler()
