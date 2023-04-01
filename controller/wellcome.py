from flask_restful import Resource


class Wellcome(Resource):
    # Message to check if the server is running
    def get(self):
        return {"Message": "Flask is Running!"}, 200
