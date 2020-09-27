# Unit 3 Sprint 2 SQL and Databases Study Guide
​
This study guide should reinforce and provide practice for all of the concepts you have seen in the past week. There are a mix of written questions and coding exercises, both are equally important to prepare you for the sprint challenge as well as to be able to speak on these topics comfortably in interviews and on the job.
​
If you get stuck or are unsure of something remember the 20 minute rule. If that doesn't help, then research a solution with [google](https://www.google.com) or [StackOverflow](https://www.stackoverflow.com). Only once you have exhausted these methods should you turn to your Team Lead - they won't be there on your SC or during an interview. That being said, don't hesitate to ask for help if you truly are stuck.
​
Have fun studying!
​
## SQL
​
**Concepts:**
​
1. What is SQL?
2. What is a RDBMS? Relational Database Managemnet system
3. What is an ETL pipeline?
4. What is a schema?
5. What does each letter in ACID stand for? Give an explanation for each and why they matter?
	- **A** Automicity- each step (unit) must complete without error for a change to be made. (Transactions)
	- **C** Consistency- must comply to all defined rules. (required fields in a form) 
	- **I** Isolation- All processes must be completed in the order they are recieved (Block chain)
	- **D** Durability- all commited changes will endure a sytem failure (server crash)

6. Explain each of the table relationships and give an example for each
	- One-to-One One instance per instance (track name to track number)
	- One-to-Many One instance may have many instances that match (Artist to albums)
	- Many-to-Many  when multiple records in a table are associated with multiple records in another table. For example, a many-to-many relationship 
exists between customers and products: customers can purchase various albums, and albums can be purchased by various customers.)
​
## Syntax
For the following section, give a brief explanation of each of the SQL commands.
​
1. **SELECT** - which columns (features) to display from the database
2. **WHERE** - preceeds conditional argument
3. **LIMIT** - limits results to a specified amount of rows (observations)
4. **ORDER** - preceeds the column(s) which the results will organize in either ascending or descending order
5. **JOIN** - combines data from two tables ON a specified collumn data that exists in both tables
6. **CREATE TABLE** - Begins a new table
7. **INSERT** - adds data to a table
8. **DISTINCT** - similar to "unique" in pandas refers to only unique values in a column. COUNT DISTINCT would be like nunique and return the number of unique values
9. **GROUP BY** - Collects (aggregates) values in a specified column to perform agregate functions on ungrouped columns. for instance Average test score grouped by sex.
10. **ORDER BY** - same as above. ORDER always needs BY to determine how the ordering is done.
11. **AVG** - an aggregate function that returns the average of a column or group.
12. **MAX** - Returns the highest value (or latest alphabetical value) of a column
13. **AS** - used to Alias a column, or table AS whatever comes after the command
​
## Starting From Scratch
Create a file named `study_part1.py` and complete the exercise below. The only library you should need to import is `sqlite3`. Don't forget to be PEP8 compliant!
1. Create a new database file call `study_part1.sqlite3`
2. Create a table with the following columns
    ```
    student - string
    studied - string
    grade - int
    age - int
    sex - string
    ```
​
3. Fill the table with the following data
​
    ```
    'Lion-O', 'True', 85, 24, 'Male'
    'Cheetara', 'True', 95, 22, 'Female'
    'Mumm-Ra', 'False', 65, 153, 'Male'
    'Snarf', 'False', 70, 15, 'Male'
    'Panthro', 'True', 80, 30, 'Male'
    ```
​
4. Save your data. You can check that everything is working so far if you can view the table and data in DBBrowser
​
5. Write the following queries to check your work. Querie outputs should be formatted for readability, don't simply print a number to the screen with no explanation, add context.
​
    ```
    What is the average age? Expected Result - 48.8
    What are the name of the female students? Expected Result - 'Cheetara'
    How many students studied? Expected Results - 3
    Return all students and all columns, sorted by student names in alphabetical order.
    ```
​
## Query All the Tables!
​
### Setup
Before we get started you'll need a few things.
1. Download the [Chinook Database here](https://github.com/bundickm/Study-Guides/blob/master/data/Chinook_Sqlite.sqlite)
2. The schema can be [found here](https://github.com/bundickm/Study-Guides/blob/master/data/Chinook%20Schema.png)
3. Create a file named `study_part2.py` and complete the exercise below. The only library you should need to import is `sqlite3`. Don't forget to be PEP8 compliant!
4. Add a connection to the chinook database so that you can answer the queries below.
​
### Queries
**Single Table Queries**
1. Find the average invoice total for each customer, return the details for the first 5 ID's SELECT Customer, AVG(Total) FROM table GROUP BY Customer LIMIT 5
2. Return all columns in Customer for the first 5 customers residing in the United States SELECT * From Table WHERE Country = 'US' LIMIT 5
3. Which employee does not report to anyone? ME!
4. Find the number of unique composers SELECT COUNT DISTINCT Composers FROM Table
5. How many rows are in the Track table? SELECT COUNT ID FROM Table
​
**Joins**
​
6. Get the name of all Black Sabbath tracks and the albums they came off of
7. What is the most popular genre by number of tracks?
8. Find all customers that have spent over $45
9. Find the first and last name, title, and the number of customers each employee has helped. If the customer count is 0 for an employee, 
it doesn't need to be displayed. Order the employees from most to least customers.
10. Return the first and last name of each employee and who they report to
​
## NoSQL
​
### Questions of Understanding
​
1. What is a document store? a database that stores each record and it's associated data in a separate document.
​
2. What is a `key:value` pair? What data type in Python uses `key:value` pairs? It is a structure that assigns a value (String, Boolean, Integer, Float, Set) to each Key that can be used to access it later. It's basically a pointer. dict (dictionary) is an example in Python.
​
3. Give an example of when it would be best to use a SQL Database and when it would be best to use a NoSQL Database Sql databases would be best used when you have multiple users inputting data and maintaining structure is important (Bank custotmer data). NoSQL might be better fit for when databases are more freeform and new features may be added at any time (Creating characters in a RPG)
​
4. What are some of the trade-offs between SQL and NoSQL? Horzontal (NoSQL) vs Vertical (SQL) scalability. NoSQL works better with unstructured data (JSON files, Document Stores), SQL works better with Structured data (Tables). SQL 
​
5. What does each letter in BASE stand for? Give an explanation for each and why they matter?
    	(B)asically 
	(A)vailable: basic reading and writing operations are available as much as possible, but without any kind of consistency guarantees 
	(the write may not persist after conflicts are reconciled, the read may not get the latest write)
	(S)oft state: without consistency guarantees, after some amount of time, we only have some probability of knowing the state, since it may not yet have 		      converged
	(E)ventually consistent: If the system is functioning and we wait long enough after any given set of inputs, we will eventually be able to know what the state 				 of the database is, and so any further reads will be consistent with our expectations