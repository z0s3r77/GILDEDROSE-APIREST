from domain.ItemList import listItems
from domain.items.AgedBrie import AgedBrie
from domain.items.Backstage import Backstage
from domain.items.Conjured import Conjured
from domain.items.NormalItem import NormalItem
from domain.items.Sulfuras import Sulfuras
from repository.MongoRepository import MongoRepository

dabatase = MongoRepository('gildedRose', 'magicalitems')


def insertItem(item):
    """
    This method inserts an item into database. RETURNS: Boolean
    """
    return dabatase.create(item)


def takeItem(id):
    """
    This method make a request to CRUD and returns parsed dict. RETURNS: Item JSON
    """
    item = dabatase.read(id)

    return item


def parseItem(item):
    """
    This method is for be sure that the item have a correct Format. RETURNS: Item JSON
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
    This method take an id a returns an item Json. RETURN: Item JSON
    """
    item = takeItem(id)
    result = parseItem(item)

    return result


def deleteItem(id):
    """
    This method delete an item from database. RETURN: Boolean
    """
    return dabatase.delete(id)


def setItemJsonToInstace(itemJson):
    """
    This method takes an itemJson, and it converted in an Item from modules. RETURNS: Item Instance
    """
    avaliableObjects = {
        "Aged Brie": AgedBrie,
        "Sulfuras of Asgard": Sulfuras,
        "Backstage passes to a TAFKAL80ETC concert": Backstage,
        "Conjured Mana Cake": Conjured
    }

    item_class = avaliableObjects.get(itemJson['name'], NormalItem)
    item_instance = item_class(name=itemJson['name'], sell_in=itemJson['sell_in'], quality=itemJson['quality'])
    return item_instance


def setJsonItem(itemInstance, id):
    """
    This method transforms an Item Instance into a JSON format, RETURN: Json Format
    """
    result = {
        "_id": id,
        "name": itemInstance.getName(),
        "sell_in": itemInstance.getSell_in(),
        "quality": itemInstance.getQuality()
    }

    return result


def updateItem(id):
    """
    This method take and ID and updates his values at the database. RETURN : Boolean
    """

    someItem = getItem(id)
    itemInstance = setItemJsonToInstace(someItem)
    itemInstance.updateQuality()
    itemToJson = setJsonItem(itemInstance, id)

    return dabatase.update(id, itemToJson)


def getAllItems():
    """
    This method return all the available items in the database. RETURN: List
    """
    result = dabatase.read()
    return result


def updateAllItems():
    """
    This method take all the Items and make them update. RETURN: List
    """
    result = dabatase.read()

    for item in result:
        updateItem(item['_id'])

    result = dabatase.read()
    return result


def intializeDb():
    """
    This method creates a new DB in the DB service and a new tabler/collection
    and inserts the items
    """
    for item in listItems:
        dabatase.create(item)

    return True


def dropCollection():
    """
    This method remove all the data in the DB
    """
    dabatase.dropCollection()

