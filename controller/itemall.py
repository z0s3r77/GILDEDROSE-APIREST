from flask_restful import Resource

from service.service import getAllItems


class ItemAll(Resource):
    def get(self):
        allItems = getAllItems()
        return allItems, 200
