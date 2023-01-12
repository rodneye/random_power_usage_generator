import random
import json
import datetime
import pymongo
from time import sleep

# Generate random values between the ()
def generate_power_monitoring_reading():
    now = datetime.datetime.now()
    timestamp = now.isoformat()
    voltage = random.uniform(230, 240)
    current = random.uniform(0, 30)
    power = voltage * current
    frequency = random.uniform(49, 51)

    return {
        "timestamp": timestamp,
        "voltage": voltage,
        "current": current,
        "power": power,
        "frequency": frequency
    }

# Connect to the MongoDB instance
client = pymongo.MongoClient("mongodb://admin:admin@localhost:27017/")
db = client["power-monitoring"]

# Select the collection where the readings will be stored
readings_collection = db["power_monitoring"]

# Generate number of readings and write to DB
readings = []
while len(readings) < 1: # Change value to generate more results
    reading = generate_power_monitoring_reading()
    readings.append(reading)
    sleep(2)
    print((reading))
    readings_collection.insert_one(reading)
    print("Data Uploaded")




