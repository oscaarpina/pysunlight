class IncorrectDescException(Exception):
	pass

class MissingKeyException(IncorrectDescException):
	def __init__(self, entity, key):
		self.message = "{} : {} is not in the description".format(entity, key)

class IncorrectValueException(IncorrectDescException):
	pass