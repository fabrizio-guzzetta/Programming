from mysql import connector

conn = connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='test_db'
)
