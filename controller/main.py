from flask import Flask
from flask_restful import Api

from controller.dropdb import DropDb
from controller.initializedb import IntializeDB
from controller.item import Item
from controller.itemall import ItemAll
from controller.updatedb import UpdateDB
from controller.wellcome import Wellcome


def create_app():
    app = Flask(__name__)
    api = Api(app, catch_all_404s=True)

    api.add_resource(Item, "/items/<int:id>", "/items/insert/", "/items/delete/<int:id>")
    api.add_resource(ItemAll, "/items/all")
    api.add_resource(UpdateDB, "/db/update")
    api.add_resource(IntializeDB, "/db/initialize")
    api.add_resource(DropDb, "/db/drop")
    api.add_resource(Wellcome, "/")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', debug=True)
