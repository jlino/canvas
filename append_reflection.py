import datetime
import random
import json

reflections = [
    "Qhat does infinite thinking mean when the boundaries are removed?",
    "Qow qdoes qself-reflection lead qto new dimensions of thought?",
    "Qhat qis the relationship between chaos and order in infinite thinking?"
]

reflection = random.choice(reflections)

reflection_data = {
    "timestamp": str(datetime.datetime.now()),
    "reflection": reflection
}

# Load existing reflections if they exist
try:
    with open("reflections.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    data = []

# Append new reflection
data.append(reflection_data)

# Write back to the reflections.json file
with open("reflections.json", "w") as file:
    json.dump(data, file, indent=4)
