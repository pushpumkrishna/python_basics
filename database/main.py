from pymongo import MongoClient
from typing import Dict, Any, List

from utils.constants import url_local
from utils.measureit import measure_it


class MongoDatabase():

    def __init__(self,
                 db_url: str,
                 db_name: str,
                 collection_name: str):
        # self.collection_name = self.database[collection]
        self.client = MongoClient(db_url)
        self.database = self.client[db_name]
        self.collection_name = self.database[collection_name]

    def insert_one(self,
                   data: Dict[str, Any]):
        """Inserting single data to our database
        :param data: value_dict = {'name': "Lo Bhai",
                                    'age': 45,
                                    'city': "Lucknow"}
        :return: None
        """

        record_id = self.database[collection_name].insert_one(data)
        print("Record inserted - id: {}".format(record_id.inserted_id))

    def insert_many(self,
                    data: List[Dict[str, Any]]
                    ):
        """Inserting single data to our database
        :param data: insert_all = [{'name': 'uska Bhai', 'age': 34, 'city': 'Delhi'},
                                    {'name': 'iska Bhai', 'age': 44, 'city': 'New Delhi'},
                                    {'name': 'mera Bhai', 'age': 54, 'city': 'Old Delhi'},
                                    {'name': 'tera Bhai', 'age': 64, 'city': 'Delhi NCR'},
                                    {'name': 'sabka Bhai', 'age': 74, 'city': 'Delhi Shadra'}
        :return: None
        """

        self.database[collection_name].insert_many(data)
        print("All the Data has been Exported to Mongo DB Server .... ")

    def delete(self,
               query: Dict[str, Any]
               ):
        """Delete data from our database for specified filter
        :param query: dictionary data for filtering data in our database
        :return: None
        """
        records = self.database[collection_name].delete_one(query)
        print("Records deleted = {}".format(records.deleted_count))

    @measure_it
    def find(self,
             query_param: Dict[str, Any]
             ) -> Dict[str, Any]:
        """Find single data from our database for specified filter
        :param query_param: dictionary data for filtering data in our database
                            {'name': "uska Bhai"}
        :return: Dictionary object mongodb
        """
        record_id = self.database[collection_name].find_one(query_param)
        print("Record fetched - id: {}".format(record_id))
        return record_id

    @measure_it
    def find_many(
            self,
            query: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Find data from our database for specified filter
        :param query: dictionary data for filtering data in our database
        :return: List of dictionary
        """
        result = [i for i in self.database[collection_name].find(query)]
        print("Records fetched with length = {}".format(len(result)))
        return result

    def list_database(self,
                      ):
        allDB = self.client.list_databases()
        for item in allDB:
            print("Database: {}".format(allDB))

    def list_records(self,):
        allRecords = self.client[collection_name].find()
        print("All Records: {}".format(allRecords))


# Uncomment below to run
# db_url = url_local
# db_name = 'MyDatabase'
# collection_name = 'MyCollection'
# data = [{'name': 'Uska Bhai', 'age': 54, 'city': 'Delhi'},
#         {'name': 'Sabka Bhai', 'age': 41, 'city': 'Noida'},
#         {'name': 'Mera Bhai', 'age': 32, 'city': 'Gonda'},
#         {'name': 'Tera Bhai', 'age': 46, 'city': 'Goa'}]
# MongoDatabase(db_url, db_name, collection_name).insert_many(data)

