import sqlite3
import pandas as pd

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()
def get_data(query, conn):
    '''Function to get data from SQLite DB'''

    cursor = conn.cursor()
    result = cursor.execute(query).fetchall()

    # Get columns from cursor object
    columns = list(map(lambda x: x[0], cursor.description))

    # Assign to DataFrame
    df = pd.DataFrame(data=result, columns=columns)
    return df
#Part 3 questions

q1= get_data('''SELECT
                    ProductName,
                    UnitPrice
                FROM
                    Product
                ORDER BY
                    UnitPrice DESC
                LIMIT
                    10;''', conn)
q2= get_data('SELECT AVG(HireDate-BirthDate) FROM Employee;', conn)
#Part 4 questions

q3= get_data('''SELECT
                    ProductName,
                    UnitPrice,
                    CompanyName AS Supplier
                FROM
                    Product
                    JOIN Supplier ON SupplierId = Supplier.id
                ORDER BY
                    UnitPrice DESC
                LIMIT
                    10;''', conn)

q4= get_data('''SELECT
                    CategoryName,
                    COUNT(DISTINCT Product.Id) as TotalProducts
                FROM
                    Product JOIN Category ON Product.CategoryId = Category.Id
                GROUP BY
                    Product.CategoryId
                ORDER BY
                    TotalProducts DESC;''', conn) #Still not working but time is up

print('Table with 10 most expensive items :')
print(q1)
print('Average age of employee at hire : ' + str(q2['AVG(HireDate-BirthDate)'][0]))
print('Table with 10 most expensive items and their suppliers:')
print(q3)
print('Table with each category and the amount of items in each')
print(q4)
print('The Confections category contains the most items.')
'''
Output =

Table with 10 most expensive items :
               ProductName  UnitPrice
0            Côte de Blaye     263.50
1  Thüringer Rostbratwurst     123.79
2          Mishi Kobe Niku      97.00
3   Sir Rodney's Marmalade      81.00
4         Carnarvon Tigers      62.50
5     Raclette Courdavault      55.00
6    Manjimup Dried Apples      53.00
7           Tarte au sucre      49.30
8              Ipoh Coffee      46.00
9        Rössle Sauerkraut      45.60
Average age of employee at hire : 37.22222222222222
Table with 10 most expensive items and their suppliers:
               ProductName  UnitPrice                           Supplier
0            Côte de Blaye     263.50         Aux joyeux ecclésiastiques
1  Thüringer Rostbratwurst     123.79  Plutzer Lebensmittelgroßmärkte AG
2          Mishi Kobe Niku      97.00                      Tokyo Traders
3   Sir Rodney's Marmalade      81.00           Specialty Biscuits, Ltd.
4         Carnarvon Tigers      62.50                      Pavlova, Ltd.
5     Raclette Courdavault      55.00                       Gai pâturage
6    Manjimup Dried Apples      53.00                        G'day, Mate
7           Tarte au sucre      49.30                   Forêts d'érables
8              Ipoh Coffee      46.00                       Leka Trading
9        Rössle Sauerkraut      45.60  Plutzer Lebensmittelgroßmärkte AG
Table with each category and the amount of items in each
     CategoryName  TotalProducts
0     Confections             13
1       Beverages             12
2      Condiments             12
3         Seafood             12
4  Dairy Products             10
5  Grains/Cereals              7
6    Meat/Poultry              6
7         Produce              5
The Confections category contains the most items.

Process finished with exit code 0
'''
curs.close()
conn.close()