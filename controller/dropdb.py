from flask_restful import Resource

from service.service import dropCollection


class DropDb(Resource):

    def get(self):
        dropCollection()
        return {"Message": "GildedRose is Closed!"}, 200
