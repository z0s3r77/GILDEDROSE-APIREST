import json
from repository import crud as CRUD


def getItem(name):
    """
    This method make a request to CRUD and returns a JSON result.
    """
    item = CRUD.read(name)
    result = json.dumps(item, indent=2)

    return result
