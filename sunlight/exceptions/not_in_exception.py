class NotInBuildingException(Exception):
	def __init__(self, building_name, apartment_number):
		self.message = "The apartment number {} is not in building {}".format(apartment_number, building_name)
class NotInNeighborhoodException(Exception):
	def __init__(self, neighborhood_name, building_name):
		self.message = "The building {} is not in {}".format(building_name, neighborhood_name)

class NotInCityException(Exception):
	def __init__(self, neighborhood_name):
		self.message = "The neighborhood {} is not in the city".format(neighborhood_name)
