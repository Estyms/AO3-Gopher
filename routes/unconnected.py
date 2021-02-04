import pituophis
from classes.User import User

def UnconnectedRoutes(request: pituophis.Request, userCache):
	if request.path=="/":
		return pituophis.Item('i',"BIENVENUE SUR AO3")
	if request.path=="/connect":
		x = User()
		userCache[x.id] = x
		return [
			pituophis.Item("i","You are now connected as {}.".format(x.id)),
			pituophis.Item("i",""),
			pituophis.Item("1","Continue","/connected/{}/".format(x.id),"localhost",7000)
		]
