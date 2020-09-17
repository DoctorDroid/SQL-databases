import sqlite3
import pandas as pd

conn = sqlite3.connect('rpg_db.sqlite3')
cursor = conn.cursor()

def get_data(query, conn):
    '''Function to get data from SQLite DB'''

    cursor = conn.cursor()
    result = cursor.execute(query).fetchall()

    # Get columns from cursor object
    columns = list(map(lambda x: x[0], cursor.description))

    # Assign to DataFrame
    df = pd.DataFrame(data=result, columns=columns)
    return df

q = get_data('SELECT COUNT(character_id) FROM charactercreator_character', conn)
q0 = get_data('SELECT COUNT(item_id) FROM charactercreator_character_inventory', conn)
q1 = get_data('SELECT COUNT(DISTINCT item_id) FROM charactercreator_character_inventory', conn)
q2 = get_data('SELECT COUNT(character_ptr_id) FROM charactercreator_cleric;', conn)
q3 = get_data('SELECT COUNT(character_ptr_id) FROM charactercreator_fighter;', conn)
q4 = get_data('SELECT COUNT(character_ptr_id) FROM charactercreator_mage;', conn)
q5 = get_data('SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer;', conn)
q6 = get_data('SELECT COUNT(character_ptr_id) FROM charactercreator_thief;', conn)
q7 = get_data('SELECT character_id, COUNT(DISTINCT id) as num_of_items '+
              'FROM charactercreator_character_inventory GROUP BY '+
              'character_id LIMIT 20;', conn)
q8 = get_data('SELECT COUNT(character_ptr_id) FROM charactercreator_cleric;', conn)

print('Number of Characters : ' + str(q['COUNT(character_id)'][0]))

print('Number of Clerics : ' + str(q2['COUNT(character_ptr_id)'][0]))
print('Number of Fighters : ' + str(q3['COUNT(character_ptr_id)'][0]))
print('Number of Mages : ' + str(q4['COUNT(character_ptr_id)'][0]))
print('Number of Necromancers : ' + str(q5['COUNT(mage_ptr_id)'][0]))
print('Number of Thieves : ' + str(q6['COUNT(character_ptr_id)'][0]))

print('Total Items: ' + str(q0['COUNT(item_id)'][0]))
print('Distinct Items: ' + str(q1['COUNT(DISTINCT item_id)'][0]))
print('Table with first 20 Characters and their number of items:')
print(q7)
print('Question 8 : ' + str(q8['COUNT(character_ptr_id)'][0]))


