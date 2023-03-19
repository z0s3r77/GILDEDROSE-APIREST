import os
import pymongo
from repository.Repository import Repository


class MongoRepository(Repository):
    def __init__(self):
        self.mongo_atlas = pymongo.MongoClient(os.getenv("ATLAS"))
        self.mongo_key = os.getenv("KEY")
        self.ollivander_shop_db = self.mongo_atlas["ollivanderShop"]
        self.magical_items = self.ollivander_shop_db["magicalitems"]

    def create(self, item):
        try:
            self.magical_items.insert_one(item)
        except:
            return False
        else:
            return True

    def read(self, id):
        query = {"_id": id}

        if self.magical_items.count_documents(query) != 0:
            result = []
            for item in self.magical_items.find(query, {"_id": False}):
                result.append(item)

            return result

    def delete(self, id):

        query = {"_id": id}
        if self.magical_items.find_one_and_delete(query) is not None:
            return True
        else:
            return False

