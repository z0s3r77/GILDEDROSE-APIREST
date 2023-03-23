from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from controller.dropdb import DropDb
from controller.initializedb import IntializeDB
from controller.item import Item
from controller.itemall import ItemAll
from controller.updatedb import UpdateDB
from controller.wellcome import Wellcome


def create_app():
    app = Flask(__name__)
    CORS(app)
    api = Api(app, catch_all_404s=True)

    # Items endpoints
    api.add_resource(Item, "/items/<int:id>")
    api.add_resource(Item, "/items/update/<int:id>", endpoint="update_item")
    api.add_resource(Item, "/items/insert/", endpoint="insert_item")
    api.add_resource(Item, "/items/delete/<int:id>", endpoint="delete_item")
    api.add_resource(ItemAll, "/items/all")

    # Database endpoints
    api.add_resource(UpdateDB, "/db/update")
    api.add_resource(IntializeDB, "/db/initialize")
    api.add_resource(DropDb, "/db/drop")

    # Welcome endpoint
    api.add_resource(Wellcome, "/")

    return app
