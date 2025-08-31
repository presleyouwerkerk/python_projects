tasks = [
    {"id": 1, "title": "Python Practice", "completed": True},
    {"id": 2, "title": "Python Practice", "completed": False},
    {"id": 3, "title": "Python Practice", "completed": False},
    {"id": 4, "title": "Python Practice", "completed": True},
]

completed_tasks = []

for task in tasks:
    if task["completed"]:
        completed_tasks.append(task)

print(completed_tasks)