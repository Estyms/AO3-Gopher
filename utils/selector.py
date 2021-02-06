import pituophis
from typing import List, Dict
from classes.User import User
from expiringdict import ExpiringDict
import random
import dotenv

pituophisPage = List[pituophis.Item]


class SelectorData:
	name: str = ""
	value: int = 0
	
	def __init__(self, name: str, value: int):
		self.name = name
		self.value = value


def selector(title: str, selectorId: str, 
			 userId: str, data: List[SelectorData], userCache: ExpiringDict, request: pituophis.Request) -> pituophisPage:
	

	if selectorId not in userCache[userId].selectors:
		userCache[userId].selectors[selectorId] = []

	response: pituophisPage = [
		pituophis.Item("i", title), 
	]

	for d in data:
		print(d.value, userCache[userId].selectors[selectorId])
		entry: pituophis.Item = pituophis.Item(
			"1", 
			"[{}] {}".format('X' if (d.value in userCache[userId].selectors[selectorId])  else ' ', d.name), 
			"{}/{}/{}/{}".format(request.path,selectorId, d.value,str(random.randrange(0,0xFFFF))),
			dotenv.get_key("../","HOST"),
			70
		)
		response += [entry]
	
	response += [pituophis.Item("i","")]
	return response
	