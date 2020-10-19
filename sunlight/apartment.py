class Apartment:
	def __init__(self, building, number):
		self.__building = building
		self.__number   = number

	def get_number(self):
		return self.__number

	def get_building(self):
		return self.__building

	def get_ceil_height(self):
		return (self.get_number() + 1) * self.get_building().get_apartments_height()

	def get_floor_height(self):
		return (self.get_number()) * self.get_building().get_apartments_height()

