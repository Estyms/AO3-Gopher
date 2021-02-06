import pituophis
from classes.User import User
from typing import Dict
from utils.selectors.filters import archive_warning_ids, category_ids
from utils.selector import selector


def ConnectedRoutes(request: pituophis.Request, userCache: Dict[str,User], userID:str):
	print(request.path.split("/"))

	if (len(request.path.split("/")) > 3) and (request.path.split("/")[3] in ["archive_warning_ids","category_ids"]):
		[category, value] = request.path.split("/")[3:5]
		value = int(value)
		print(category, value)
		if value in userCache[userID].selectors[category]:
			userCache[userID].selectors[category].remove(value)
		else:
			userCache[userID].selectors[category].append(value)
		print(userCache[userID].selectors)
		request.path = '/'.join(request.path.split("/")[0:3])

	response = []
	response += selector("Warnings", "archive_warning_ids", userID, archive_warning_ids, userCache, request)
	response += selector("Categories", "category_ids", userID, category_ids, userCache, request)
	return response