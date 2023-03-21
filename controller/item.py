from flask_restful import Resource, fields, marshal_with, abort, reqparse
from service.service import getItem, insertItem, deleteItem, updateItem

item_parser = reqparse.RequestParser()
item_parser.add_argument('_id', type=int, required=True)
item_parser.add_argument('name', type=str, required=True)
item_parser.add_argument('sell_in', type=int, required=True)
item_parser.add_argument('quality', type=int, required=True)

item_fields = {
    "name": fields.String,
    "sell_in": fields.Integer,
    "quality": fields.Integer,
}


class Item(Resource):
    @marshal_with(item_fields)
    def get(self, id):
        items = getItem(id)
        if items == {"name": "", "sell_in": 0, "quality": 0}:
            abort(404, message="The item with {} doesn't exist".format(id))
        return items, 200

    def post(self):
        item = item_parser.parse_args()
        success = insertItem(item)
        if success:
            return {"Message": "The item has been introduced with id {}".format(item['_id'])}, 200
        else:
            return {"Message": "The item has not been introduced, maybe is already at the DB"}, 400

    def put(self, id):
        success = updateItem(id)
        if success:
            return {"Message": "The item have been updated"}, 200


    def delete(self, id):
        success = deleteItem(id)
        if success:
            return {"Message": "The item has been deleted with id {}".format(id)}, 200
        else:
            return {"Message": "The item is not in the DB"},400


