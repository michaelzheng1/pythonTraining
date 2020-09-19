import mysql.connector

con = mysql.connector.connect(
    user="", 
    password = "",
    host="",
    database = ""
)

cursor = con.cursor()

word = input("Enter a word: ")
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(results[1])
else:
    print("No word found!")