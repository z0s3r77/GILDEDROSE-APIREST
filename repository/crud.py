import pymongo
import os

MongoAtlas = pymongo.MongoClient(os.getenv("ATLAS"))
MongoKey = os.getenv("KEY")


def read(id):
    """
    This method return a LIST with the items which name is indicated
    """
    ollivanderShopDb = MongoAtlas["ollivanderShop"]
    magicalItems = ollivanderShopDb["magicalitems"]

    query = {"_id": id}

    if magicalItems.count_documents(query) != 0:
        result = []
        for item in magicalItems.find(query, {"_id": False}):
            result.append(item)

        return result
