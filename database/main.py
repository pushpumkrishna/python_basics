from database.mongo import MongoDatabase
from utils.constants import url_local


db_url = url_local
db_name = 'MyDatabase'
collection_name = 'MyCollection'
data = [{'name': 'Uska bada Bhai', 'age': 54, 'city': 'Delhi'},
        {'name': 'Sabka bada Bhai', 'age': 41, 'city': 'Noida'},
        {'name': 'Mera bada Bhai', 'age': 32, 'city': 'Gonda'},
        {'name': 'Tera bada Bhai', 'age': 46, 'city': 'Goa'}]
query = {'name': 'Tera bada Bhai'}
query_many = {'name': 'Tera bada Bhai'}

MongoDatabase(db_url, db_name, collection_name).list_database()
MongoDatabase(db_url, db_name, collection_name).list_records()
MongoDatabase(db_url, db_name, collection_name).insert_one(query)
MongoDatabase(db_url, db_name, collection_name).insert_many(data)
MongoDatabase(db_url, db_name, collection_name).find_one(query)
MongoDatabase(db_url, db_name, collection_name).find_many(query_many)
MongoDatabase(db_url, db_name, collection_name).delete(query)
