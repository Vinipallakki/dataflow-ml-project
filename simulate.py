from google.cloud import pubsub_v1
import time
import json
import random

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path("nimble-courier-449405-f7", "sensor-data-topic")

def generate_data():
    return {
        "timestamp": time.time(),
        "machine_id": random.randint(1, 5),
        "temperature": round(random.uniform(30, 100), 2),
        "vibration": round(random.uniform(0.1, 5.0), 2),
        "pressure": round(random.uniform(1.0, 10.0), 2)
    }

while True:
    data = json.dumps(generate_data()).encode("utf-8")
    publisher.publish(topic_path, data)
    print("Published:", data)
    time.sleep(1)  # send 1 message per second



