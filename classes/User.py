import random
import crypt
from expiringdict import ExpiringDict

class User():
	# VAR
	id = ""
	search_query=[]

	# Constructor
	def __init__(self):
		rng = str(random.randrange(0,0xFFFFFFFF))
		crypted = crypt.crypt(rng,crypt.METHOD_CRYPT)
		self.id = ''.join(filter(str.isalnum,crypted))


userCache = ExpiringDict(0xFFFF, 3600)
