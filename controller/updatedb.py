from flask_restful import Resource

from service.service import updateAllItems


class UpdateDB(Resource):
    def get(self):
        allItems = updateAllItems()
        return allItems, 200
