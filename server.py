import pituophis
from classes.User import User, userCache

from routes.unconnected import UnconnectedRoutes
from routes.connected import ConnectedRoutes



#REQUEST HANDLER
def requestHandler(request: pituophis.Request):

    # IF CLIENT IS CONNECTED
    if "/connected/" in request.path:
        print(request.path)
        user : User = userCache.pop(request.path.split("/")[2])
        userCache[user.id] = user
        return ConnectedRoutes(request, userCache, user.id)

    # IF CLIENT NOT CONNECTED
    else:
        return UnconnectedRoutes(request, userCache)

    


pituophis.serve('localhost', 70, pub_dir="pub/", alt_handler=requestHandler)