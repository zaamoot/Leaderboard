import sqlite3

connection = sqlite3.connect("Leaderboard.db")

# create tables for SQLite database
cursor = connection.cursor()
cursor.execute("CREATE TABLE Games (GameID INTEGER, TeamID1 INTEGER, TeamID2 INTEGER)")



print(connection.total_changes)