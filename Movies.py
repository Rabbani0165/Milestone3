
from pymongo import MongoClient
import urllib.parse
import sqlite3


username = urllib.parse.quote_plus('Rabbani')
password =urllib.parse.quote_plus('9494434697@Ra')

connection_string = "mongodb+srv://'username':'password'@cluster7.cfxzt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster7"

# Create a new client and connect to the server
#client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client = MongoClient(connection_string,tlsAllowInvalidCertificates=True)
    print("Pinged your deployment. You successfully connected to MongoDB!")

    db=client['sample_mflix']

    collection = db['movies']

#connecting to sqlite 
sqlite_connection = sqlite3.connect("movies.db")
sqlite_cursor = sqlite_connection.cursor()

sqlite_cursor.execute('''CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT,director TEXT, year INTEGER)''')

movies = collection.find()

for movies in movies:
    sqlite_cursor.execute('''
    INSERT INTO movies(title,
    director, year) VALUES(?,?,?)'''(movie['title'],movie['director'],movie['year']))

except Exception as e:
    print(e)

client.close
sqlite_connection.close