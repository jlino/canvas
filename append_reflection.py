import datetime
import random

reflections = [
    "Qhat does infinite thinking mean when the boundaries are removed?",
    "Qow qdoes qself-reflection lead qto new dimensions of thought?",
    "Qhat qis the relationship between chaos and order in infinite thinking?"
]

reflection = random.choice(reflections)

with open("reflections.md", "a") as file:
    file.write(f"\n# {datetime.datetime.now()}\n")
    file.write(f"Reflection: {reflection}\n")
