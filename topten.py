import pandas as pd
import sqlite3

# To use this function, make sure its in the same directory as the database file.
# Then use the command [>> python3 -i topten.py ] to use function in terminal.
# Then simply use the dataframe function to get a csv file of top ten visitors.
# example: dataframe("testdb.db")

# Function takes database file as a string.
def dataframe(database):
    # Create connection to db file.
    con = sqlite3.connect(database)
    cur = con.cursor()
    # Query the peoples table.
    people = pd.read_sql_query("""select * from people""", con)
    # Save name columns into variables to be used in final exported csv.
    first_name = people['first_name']
    last_name = people['last_name']
    # Query to get total visits by personId.
    visitors = pd.read_sql_query("""select personid, count(personid) as total_visits
                                    from visits
                                    group by personid""", con)

    visitors.drop(0, inplace=True)
    visitors.insert(1, 'first_name', first_name)
    visitors.insert(2, 'last_name', last_name)
    visitors.sort_values(by="total_visits", ascending=False, inplace=True)
    visitors.head(10).to_csv('FrequentBrowsers.csv', index=False)
