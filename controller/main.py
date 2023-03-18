from flask import Flask
from flask_restful import Resource, Api, fields, marshal_with, abort
from service.crudMain import getItem

app = Flask(__name__)
api = Api(app)


class Item(Resource):
    item_fields = {
        "name": fields.String,
        "sell_in": fields.Integer,
        "quality": fields.Integer,
    }

    @marshal_with(item_fields)
    def get(self, id):
        items = getItem(id)
        if items == {"name": "", "sell_in": 0, "quality": 0}:
            abort(404, message="The item with {} doesn't exist".format(id))
        return items, 200


class Main(Resource):
    def get(self):
        return "<h1>FLASK-API-REST Olivanders</h1>"


api.add_resource(Item, "/items/<int:id>")
api.add_resource(Main, "/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
