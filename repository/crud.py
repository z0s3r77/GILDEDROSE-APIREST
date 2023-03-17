from repository.MongoAtlasConexion import MongoAtlas


def read(name):
    """
    This method return a LIST with the items which name is indicated
    """
    ollivanderShopDb = MongoAtlas["ollivanderShop"]
    magicalItems = ollivanderShopDb["magicalitems"]

    query = {"name": name}

    if magicalItems.count_documents(query) != 0:
        result = []
        for item in magicalItems.find(query, {"_id": False}):
            result.append(item)

        return result
