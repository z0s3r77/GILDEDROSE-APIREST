from flask_restful import Resource


class Wellcome(Resource):


    def get(self):
        return "<h1>FLASK-API-REST Olivanders</h1>"
