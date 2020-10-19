from .neighborhood import Neighborhood
from .exceptions.not_in_exception import NotInCityException

class City:
	"""
	def __init__(self, desc):
		self.__neighborhoods = dict()
		for n in desc:
			Neighborhood.is_description_correct(n)
			neighborhood = Neighborhood(n)
			self.__neighborhoods[neighborhood.get_name()] = (neighborhood)
	"""
	def __init__(self, neighborhoods):
		self.__neighborhoods = dict()
		for n in neighborhoods:
			self.__neighborhoods[n.get_name()] = n

	@classmethod
	def is_description_correct(cls, desc):
		#for n in desc:
		#	Neighborhood.is_description_correct(n)
		return True

	def is_in_city(self, neighborhood_name):
		if neighborhood_name not in self.__neighborhoods:
			raise NotInCityException(neighborhood_name)
		return True

	def get_neighborhood(self, neighborhood_name):
		self.is_in_city(neighborhood_name)
		return self.__neighborhoods[neighborhood_name]

	def get_building(self, neighborhood_name, building_name):
		return self.get_neighborhood(neighborhood_name).get_building(building_name)

	def get_eastern_buildings(self, neighborhood_name, building_name):
		return self.get_neighborhood(neighborhood_name).get_eastern_buildings(building_name)

	def get_western_buildings(self, neighborhood_name, building_name):
		return self.get_neighborhood(neighborhood_name).get_western_buildings(building_name)

	def get_apartment(self, neighborhood_name, building_name, apartment_number):
		return self.get_neighborhood(neighborhood_name).get_apartment(building_name, apartment_number)


