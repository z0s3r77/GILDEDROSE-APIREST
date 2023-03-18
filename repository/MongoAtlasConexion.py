import urllib.request


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


if not connect(host="https://www.mongodb.com/atlas/app-services/data-api"):
    quit()
