import pdb
from models.task import Task
import repositories.task_repository as task_repository 

# --- test db delete, read, write ---
task_repository.delete_all()

task_1 = Task('2022-01-01 00:00:00', 10, 'A')
task_repository.save(task_1)

result = task_repository.select_all()

for task in result:
    print(task.__dict__)

pdb.set_trace()