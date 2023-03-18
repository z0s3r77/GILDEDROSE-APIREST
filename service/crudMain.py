from repository import crud as CRUD


def readItem(id):
    """
    This method make a request to CRUD and returns parsed dict.
    Get an ID and return dict
    """
    item = CRUD.read(id)

    return item


def parseItem(item):
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
    item = readItem(id)
    result = parseItem(item)

    return result
