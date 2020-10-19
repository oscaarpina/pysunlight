from .building import Building
from .exceptions.incorrect_desc_exception import MissingKeyException
from .exceptions.not_in_exception import NotInNeighborhoodException

class Neighborhood:

	N_NAME_KEY = "neighborhood"
	N_APARTMENTS_HEIGHT_KEY = "apartments_height"
	N_BUILDINGS_KEY = "buildings"
	"""
	def __init__(self, desc):
		self.__name = desc[self.N_NAME_KEY]
		self.__apartments_height = desc[self.N_APARTMENTS_HEIGHT_KEY]

		self.__buildings = list()
		self.__buildings_numbers = dict()
		for num,b in enumerate(desc[self.N_BUILDINGS_KEY]):
			building = Building(b, num, self.__apartments_height)
			self.__buildings.append(building)
			self.__buildings_numbers[building.get_name()] = num
	"""

	def __init__(self, name, apartments_height, buildings):
		self.__name = name
		self.__apartments_height = apartments_height

		self.__buildings = buildings
		self.__buildings_numbers = dict()
		for b in buildings:
			self.__buildings_numbers[b.get_name()] = b.get_number()


	def get_name(self):
		return self.__name

	@classmethod
	def is_description_correct(cls, desc):
		for f in [cls.N_NAME_KEY, cls.N_APARTMENTS_HEIGHT_KEY, cls.N_BUILDINGS_KEY]:
			if f not in desc:
				raise MissingKeyException("NEIGHBORHOOD", f)

		#for b in desc[self.N_BUILDINGS_KEY]:
		#	Building.is_description_correct(b)
		return True

	def is_in_neighborhood(self, building_name):
		if building_name not in self.__buildings_numbers:
			raise NotInNeighborhoodException(self.get_name(), building_name)
		return True

	def get_building_number(self, building_name):
		self.is_in_neighborhood(building_name)
		return self.__buildings_numbers[building_name]

	def get_building(self, building_name):
		return self.__buildings[self.get_building_number(building_name)]

	def get_eastern_buildings(self, building_name):
		return self.__buildings[:self.get_building_number(building_name)]

	def get_western_buildings(self, building_name):
		n = self.get_building_number(building_name)
		return self.__buildings[n+1:] if n+1 < len(self.__buildings) else list()

	def get_apartment(self, building_name, apartment_number):
		return self.get_building(building_name).get_apartment(apartment_number)