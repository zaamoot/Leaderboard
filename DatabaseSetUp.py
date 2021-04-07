import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('Leaderboard.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists
cursor.execute("DROP TABLE IF EXISTS Games")
print("Table Games dropped ")

#Creating table as per requirement
sql ='''CREATE TABLE Games(
   GameID INTEGER NOT NULL,
   PlayerID INTEGER,
   TeamID INTEGER,
   Score INTEGER,
   RankUpdate INTEGER
)'''
cursor.execute(sql)
print("Table created successfully........")

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()