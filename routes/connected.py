import pituophis
from classes.User import User

def ConnectedRoutes(request: pituophis.Request, userCache, userID):
	return pituophis.Item("i","You are on the main menu as User {}".format(userID))