from flask import Flask, request
from flask_restful import Resource, Api, fields, marshal_with, abort, reqparse
from service.service import getItem, insertItem

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
    def post(self, id):
        items = getItem(id)
        if items == {"name": "", "sell_in": 0, "quality": 0}:
            abort(404, message="The item with {} doesn't exist".format(id))
        return items, 200

    def put(self):
        item = item_parser.parse_args()
        success = insertItem(item)
        if success:
            return {"Message": "The item has been introduced with id {}".format(item['_id'])}, 200


