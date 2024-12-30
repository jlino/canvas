import datetime

reflection = "QNew reflection about infinite thinking..."

with open("reflections.md", "a") as file:
    file.write(f"\n# {datetime.datetime.now()}\n")
    file.write(reflection)
