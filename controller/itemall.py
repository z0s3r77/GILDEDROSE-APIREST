from flask_restful import Resource

from service.service import getAllItems


class ItemAll(Resource):
    def get(self):
        allItems = getAllItems()
        if not allItems:
            # 404 not found
            return {"Error Message": "The items are not in the DB, intialize with /db/initialize"}, 404
        # 200 ok
        return allItems, 200
