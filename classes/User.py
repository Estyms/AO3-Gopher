import random
import crypt
from expiringdict import ExpiringDict
from typing import List, Dict

class User():
	# VAR
	id = ""
	selectors : Dict[str, List[int]] = {}

	# Constructor
	def __init__(self):
		rng = str(random.randrange(0,0xFFFFFFFF))
		crypted = crypt.crypt(rng,crypt.METHOD_CRYPT)
		self.id = ''.join(filter(str.isalnum,crypted))


# User Session Cache
userCache = ExpiringDict(0xFFFF, 3600)
