import pymongo
import urllib.request


# Check conexion MongoAtlas
def connect(host):
    if host != "https://www.mongodb.com/atlas/app-services/data-api":
        print("No ha introducido la URL correcta")
        return False
    else:
        pass

    try:
        urllib.request.urlopen(host)
        return True
    except:
        print("No es posible acceder a Mongo Atlas")
        return False


if connect(host="https://www.mongodb.com/atlas/app-services/data-api") == False:
    quit()


# Modulo que guarda variables importantes

MongoAtlas = pymongo.MongoClient(
    "mongodb+srv://sestacio:trancas24@sandbox.dcnt9qr.mongodb.net/test?retryWrites=true&w=majority"
)
MongoKey = "SwVPwadBrjuOJcUQrh887SGLLUq9IGo2e6fFOPo0lQumOkRNW0xTC5v3YROR1S3T"
