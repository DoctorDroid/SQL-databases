import sqlite3
import pandas as pd

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()
curs.execute('''CREATE TABLE IF NOT EXISTS demo_table (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                 s TEXT,
                                                 x INT,
                                                 y INT);''')
curs.execute('''INSERT INTO
                demo_table(s,x,y)
                VALUES
                 ('g', 3,9),
                 ('v', 5, 7),
                 ('f', 8, 7);''')
conn.commit()
def get_data(query, conn):
    '''Function to get data from SQLite DB'''

    cursor = conn.cursor()
    result = cursor.execute(query).fetchall()

    # Get columns from cursor object
    columns = list(map(lambda x: x[0], cursor.description))

    # Assign to DataFrame
    df = pd.DataFrame(data=result, columns=columns)
    return df

q1= get_data('SELECT COUNT(id) FROM demo_table', conn)
q2= get_data('SELECT COUNT(id) FROM demo_table WHERE x >= 5 AND y >= 5', conn)
q3= get_data('SELECT COUNT(DISTINCT y) FROM demo_table', conn)
print('Number of rows : ' + str(q1['COUNT(id)'][0]))
print('Number of rows : ' + str(q2['COUNT(id)'][0]))
print('Number of rows : ' + str(q3['COUNT(DISTINCT y)'][0]))

'''
Number of rows : 3
Number of rows : 2
Number of rows : 2

Process finished with exit code 0
'''
curs.close()
conn.close()