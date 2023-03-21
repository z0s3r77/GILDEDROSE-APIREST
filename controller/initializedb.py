from flask_restful import Resource
from service.service import intializeDb


class IntializeDB(Resource):

    def get(self):
        intilizeDb = intializeDb()

        if intilizeDb:
            return {"Message": "GildedRose is Open!"}, 200
        else:
            return {"Error Message": "GildedRose is Closed!"}, 200
