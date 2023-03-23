from flask_restful import Resource


class Wellcome(Resource):
    def get(self):
        return {"Message": "Flask is Running!"}, 200
