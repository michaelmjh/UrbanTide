import pandas as pd
import pdb
from models.task import Task
import repositories.task_repository as task_repository 

def readData(filename):
    return pd.read_csv(f'./{filename}.csv')

def checkCategory(columnData):
    categories = ['A', 'B', 'C']
    for i in columnData:
        if i not in categories:
            return False
    return True

print('Clearing existing data from db\n')
task_repository.delete_all()

filenames = ['UrbanTide1', 'UrbanTide2']

for fn in filenames:
    commit = True
    importData = readData(fn)
    for column in importData.columns:
# If data in column is of type int, check standard deviation of column data is greater than a given value
        if importData[column].dtypes == 'int64':
            if importData[column].std() > 2:
                commit = False
                break
# If column data is a char, check it is a given list
        if (importData[column].dtypes == 'object') and (importData[column].apply(len).mean() == 1):
            commit = checkCategory(importData[column])
            if not commit:
                break
# if commit flag is true, loop through rows and save to db
    if commit:
        print(f'Save to db: {fn}')
        for id in importData.itertuples():
            new_task = Task(id[1], id[2], id[3])
            task_repository.save(new_task)
    else:
        print(f'Outlier detected: {fn}')

# Output database
result = task_repository.select_all()

print('\ndb data')
for task in result:
    print(task.__dict__)

pdb.set_trace()