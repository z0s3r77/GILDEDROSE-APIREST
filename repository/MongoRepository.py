import os
import pymongo
from repository.Repository import Repository


class MongoRepository(Repository):
    def __init__(self, nameDb, nameCollection):
        self.mongo_atlas = pymongo.MongoClient(os.getenv("ATLAS"))
        self.mongo_key = os.getenv("KEY")
        self.gildedRoseDb = self.mongo_atlas[nameDb]
        self.magical_items = self.gildedRoseDb[nameCollection]

    def create(self, item):
        try:
            self.magical_items.insert_one(item)
        except:
            return False
        else:
            return True

    def read(self, id=None):

        if id is not None:

            query = {"_id": id}

            if self.magical_items.count_documents(query) != 0:
                result = []
                for item in self.magical_items.find(query, {"_id": False}):
                    result.append(item)

                return result
        else:

            result = self.magical_items.find()
            return list(result)

    def update(self, id, updatedItem):
        filterToUpdate = {"_id": id}
        result = self.magical_items.replace_one(filterToUpdate, updatedItem)
        return result.acknowledged

    def delete(self, id):

        query = {"_id": id}
        if self.magical_items.find_one_and_delete(query) is not None:
            return True
        else:
            return False

    def dropCollection(self):
        self.magical_items.drop()
