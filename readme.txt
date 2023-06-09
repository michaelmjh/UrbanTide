Used:
- python3
- sqlite3 
- pandas
- pdb

------------------
Setup db:
sqlite3 db/task_manager.db < db/task_manager.sql

Run test to make sure db is working. 
Should retrun 1 result - {'timestamp': '2022-01-01 00:00:00', 'value': 10, 'category': 'A'}:
python3 test.py 

Run app:
python3 app.py

------------------
Approach:
1. Setup read csv and basic outlier detection app
2. Setup database and connect to app 
3. Setup Docker container and move app and database in
4. Setup web api to handle reading csv

------------------
Thoughts (09Jun23):
1.  Outlier detection is a bit of a rabbit hole and even basic detection could have included more checks. 
    For example, the category is currently being checked to see if the entry is included in a given list, but could be expanded to check string length or sequential entries.
    While it works very basically, it is currently not scalable and also works only with a very specific format of data.
    I would have also liked to bring the app code in line with SOLID principles and also implement unit testing.
2.  It's been a while since I last set up and connected a db so had to spend more time than anticipated refreshing myself on the process.
    Currently, the db is hardcoded in and it would be good to generate it programatically so it could work with differently formatted data.
    Though very very basic testing is available, I would have liked this to be more comprehensive.
3.  I have begun looking at Dockerizing this app but have not been able to implement it in the given time unfortunately.
    That said, the documentation would suggest the process is reasonably straightforward.