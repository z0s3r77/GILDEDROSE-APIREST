from flask import Flask
from flask_restful import Api
from controller.item import Item
from controller.wellcome import Wellcome


def create_app():

    app = Flask(__name__)
    api = Api(app, catch_all_404s=True)

    api.add_resource(Item, "/items/<int:id>", "/items/insert/")
    api.add_resource(Wellcome, "/")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
