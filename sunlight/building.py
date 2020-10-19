from .apartment import Apartment
from .shadow import Shadow
from .exceptions.incorrect_desc_exception import MissingKeyException, IncorrectValueException
from .exceptions.not_in_exception import NotInBuildingException

class Building:

	B_NAME_KEY = "name"
	B_APARTMENTS_COUNT_KEY = "apartments_count"
	B_DISTANCE_KEY = "distance"

	def __init__(self, name, apartments_count, distance, apartments_height):
		self.__name = name
		self.__apartments_count = apartments_count
		self.__distance = distance
		self.__apartments_height = apartments_height
		self.__number = None

		self.__apartments = list()
		for i in range(self.__apartments_count):
			apartment = Apartment(self, i)
			self.__apartments.append(apartment)

		self.__shadow = Shadow(self)


	def get_name(self):
		return self.__name

	def get_number(self):
		return self.__number

	def set_number(self, number):
		self.__number = number

	def get_distance(self):
		return self.__distance

	def get_apartments_count(self):
		return self.__apartments_count

	def get_apartments_height(self):
		return self.__apartments_height

	def get_height(self):
		return self.get_apartments_count() * self.get_apartments_height()

	def get_shadow(self):
		return self.__shadow

	@classmethod
	def is_description_correct(cls, desc):
		for f in [cls.B_NAME_KEY, cls.B_APARTMENTS_COUNT_KEY, cls.B_DISTANCE_KEY]:
			if f not in desc:
				raise MissingKeyException("BUILDING", f)

		if desc[cls.B_APARTMENTS_COUNT_KEY] <= 0:
			raise IncorrectValueException("BUILDING", "{} must be greater than 0.".format(cls.B_APARTMENTS_COUNT_KEY))

		if desc[cls.B_DISTANCE_KEY] < 0:
			raise IncorrectValueException("BUILDING", "{} must be greater than 0.".format(cls.B_DISTANCE_KEY))
		return True

	def is_in_building(self, apartment_number):
		if not (0 <= apartment_number < len(self.__apartments)):
			raise NotInBuildingException(self.get_name(), apartment_number)
		return True

	def get_apartment(self, apartment_number):
		self.is_in_building(apartment_number)
		return self.__apartments[apartment_number]