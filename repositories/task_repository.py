import re
from db.run_sql import run_sql

from models.task import Task

# Get all data from db
def select_all():  
    tasks = [] 

    sql = "SELECT * FROM tasks"
    results = run_sql(sql)

    for row in results:
        task = Task(row['timestamp'], row['value'], row['category'] )
        tasks.append(task)
    return tasks 

# Save item to db
def save(task):
    sql =f"INSERT INTO tasks (timestamp, value, category) VALUES (?, ?, ?) RETURNING *" 
    values = [task.timestamp, task.value, task.category]
    results = run_sql(sql, values)
    task.id = results[0]['id']
    return id

# Delete all data from db
def delete_all():
    sql = "DELETE FROM tasks"
    run_sql(sql)