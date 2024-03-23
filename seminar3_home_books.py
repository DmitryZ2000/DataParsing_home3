import json
from pymongo import MongoClient
from pprint import pprint
 
client = MongoClient('mongodb://localhost:27017/')
  
# #Загружаем в базу "books" коллекцию 'first
# collection = client["books"]["info"]
 
# with open('books.json') as file:
#     file_data = json.load(file)
     
# collection.insert_many(file_data)


books = client.books.info
count = 0
# найти все книги в коллекции "info" дороже 46
for entry in books.find({'price': {'$gt': 55, '$lt': 60}} ):
    count += 1
    # pprint(entry)
print(f'{count = }')

count = 0
# найти все книги в коллекции "info" дороже 46
for entry in books.find({'price': {'$gt': 55, '$lt': 60},'rating': 'One'},{'_id': 0, 'name': 1} ):
    count += 1
    # pprint(entry)
print(f'{count = }')

count = 0
# найти все книги в коллекции "info" дороже 46
for entry in books.find({'$and':[{'price': {'$gt': 55, '$lt': 60}},{'rating': 'One'}]},{'_id': 0, 'name': 1} ):
    count += 1
    pprint(entry)
print(f'{count = }')

count = 0
# найти все книги в коллекции "info" дороже 46
for entry in books.find({'$or':[{'price': {'$gt': 55, '$lt': 60}},{'rating': 'Two'}]},{'name': 1} ):
    count += 1
    # pprint(entry)
print(f'{count = }')