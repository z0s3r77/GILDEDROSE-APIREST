from domain.items.GildedRose import GildedRose
from domain.items.Item import Item
from repository.MongoRepository import MongoRepository

mongo_repo = MongoRepository()


def insertItem(item):
    """
    This method send item to CRUD and returns TRUE or FALSE
    if the item has been inserted or not
    """
    return mongo_repo.create(item)


def takeItem(id):
    """
    This method make a request to CRUD and returns parsed dict.
    Get an ID and return dict
    """
    item = mongo_repo.read(id)

    return item


def parseItem(item):
    """
    This method is for be sure that the item have a correct Format
    """
    if item:
        result = {
            "name": item[0]["name"],
            "sell_in": item[0]["sell_in"],
            "quality": item[0]["quality"],
        }
    else:
        result = {"name": "", "sell_in": 0, "quality": 0}

    return result


def getItem(id):
    """
    This method return an item, uses takeItem() and parseItem() for be SRP
    """
    item = takeItem(id)
    result = parseItem(item)

    return result



def deleteItem(id):
    """
    This method only return TRUE or FALSE if an item have been deleted
    """
    return mongo_repo.delete(id)


def updateItem(id):
    """
    This method take and ID and updates his values at the database, returns TRUE of FALSE if the item
    have been updated
    """

    someItem = getItem(id)

    items = [Item(name=someItem['name'], sell_in=someItem['sell_in'], quality=someItem['quality'])]

    itemsToParticularObject = GildedRose(items)
    itemsToParticularObject.setObjects()
    items = itemsToParticularObject.getObjects()

    GildedRose(items).update_quality()

    for item in items:

        result = {
            "_id": id,
            "name": item[0].getName(),
            "sell_in": item[0].getSell_in(),
            "quality": item[0].getQuality()
        }
        return mongo_repo.update(id, result)