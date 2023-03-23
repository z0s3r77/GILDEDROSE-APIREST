from flask_restful import Resource, abort, fields, marshal_with, reqparse

from service.service import deleteItem, getItem, insertItem, updateItem

item_parser = reqparse.RequestParser()
item_parser.add_argument("_id", type=int, required=True)
item_parser.add_argument("name", type=str, required=True)
item_parser.add_argument("sell_in", type=int, required=True)
item_parser.add_argument("quality", type=int, required=True)

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
            # 404 not found
            abort(404, message="The item with {} doesn't exist".format(id))
            # 200 ok
        return items, 200

    def put(self):
        item = item_parser.parse_args()
        success = insertItem(item)
        if success == "CREATED":
            # 201 created
            return {
                "Message": "The item has been introduced with id {}".format(item["_id"])
            }, 201
        elif success == "UPDATED":
            # 204 no content
            return 204

    def post(self, id):
        success = updateItem(id)
        if success:
            # 200 ok
            return {"Message": "The item have been updated"}, 200
        else:
            # 404 not found
            return {"Error Message": "The item with id {} not exist".format(id)}, 404

    def delete(self, id):
        success = deleteItem(id)
        if success:
            # 202 accepted
            return {"Message": "The item has been deleted with id {}".format(id)}, 202
        else:
            # 404 not found
            return {"Message": "The item is not in the DB"}, 404
