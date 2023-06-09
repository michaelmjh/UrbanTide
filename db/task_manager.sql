-- Create db
DROP TABLE IF EXISTS tasks;

CREATE TABLE tasks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  timestamp DATETIME,
  value INT,
  category VARCHAR
);