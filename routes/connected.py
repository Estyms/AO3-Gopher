import pituophis
from classes.User import User
from typing import Dict
from utils.selectors.filters import warnings, categories
from utils.selector import selector

def ConnectedRoutes(request: pituophis.Request, userCache: Dict[str,User], userID:str):
	print(request.path.split("/"))
	if (len(request.path.split("/")) > 3) and (request.path.split("/")[3] in ["warnings","categories"]):
		[category, value] = request.path.split("/")[3:5]
		print(category, value)
		userCache[userID].selectors[category] ^= int(value)
		request.path = '/'.join(request.path.split("/")[0:3])

	response = []
	response += selector("warnings", "warnings", userID, warnings, userCache, request)
	response += selector("categories", "categories", userID, categories, userCache, request)
	return response