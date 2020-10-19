from .city import City
from .neighborhood import Neighborhood
from .building import Building
import math
import time
import json

DEFAULT_RAISE_TIME  = "08:14"
DEFAULT_SETTING_TIME = "17:25"
class SunlightCalculator:

	def __init__(self, **kwargs):
		self.city = None

		raise_time   = time.strptime(DEFAULT_RAISE_TIME if "raise_time" not in kwargs else kwargs["raise_time"], "%H:%M")
		self.__raise_time = raise_time.tm_sec + 60*raise_time.tm_min + 3600*raise_time.tm_hour

		setting_time = time.strptime(DEFAULT_SETTING_TIME if "setting_time" not in kwargs else kwargs["setting_time"], "%H:%M")
		self.__setting_time = setting_time.tm_sec + 60*setting_time.tm_min + 3600*setting_time.tm_hour

		assert setting_time > raise_time, "Setting time must be larger than raise time."
		
		self.__w = math.pi/(self.__setting_time - self.__raise_time)

	def get_raise_time(self):
		return self.__raise_time

	def get_setting_time(self):
		return self.__setting_time

	def get_w(self):
		return self.__w

	def init(self, s):
		s = json.loads(s)
		self.create_city(s)

	def create_city(self, s):
		neighborhoods_list = list()
		for n in s:
			neighborhoods_list.append(self.create_neighborhood(n))
		self.city = City(neighborhoods_list)

	def create_building(self, n, b, num):
		Building.is_description_correct(b)
		return Building(b[Building.B_NAME_KEY], b[Building.B_APARTMENTS_COUNT_KEY], b[Building.B_DISTANCE_KEY], \
					num, n[Neighborhood.N_APARTMENTS_HEIGHT_KEY])

	def create_neighborhood(self, n):
		Neighborhood.is_description_correct(n)
		buildings_list = list()
		for idx, b in enumerate(n[Neighborhood.N_BUILDINGS_KEY]):
			buildings_list.append(self.create_building(n, b, idx))
		return Neighborhood(n[Neighborhood.N_NAME_KEY], n[Neighborhood.N_APARTMENTS_HEIGHT_KEY], buildings_list)

	def get_sunlight_angles(self, neighborhood_name, building_name, apartment_number):
		building  = self.city.get_building(neighborhood_name, building_name)
		apartment = self.city.get_apartment(neighborhood_name, building_name, apartment_number)

		apartment_floor, apartment_ceil = apartment.get_floor_height(), apartment.get_ceil_height()

		# STEP 1 : Compute sunlight start time

		# the sunlight will cover the east side when all the shadows have intersected with the floor -> find max
		easten_buildings = self.city.get_eastern_buildings(neighborhood_name, building.get_name())
		init_angle = 0
		for b in easten_buildings:
			angle = b.get_shadow().compute_intersection_angle(building.get_distance(), apartment_floor)
			if angle>init_angle:
				init_angle = angle

		# STEP 2 : Compute sunlight end time

		# as soon as a shadow reaches the floor, the sunlight will no more cover completely the west side -> find min
		westen_buildings = self.city.get_western_buildings(neighborhood_name, building.get_name())
		end_angle = math.pi
		for b in westen_buildings:
			angle = b.get_shadow().compute_intersection_angle(building.get_distance(), apartment_floor)
			if angle<end_angle:
				end_angle = angle
		return init_angle, end_angle

	def angle2time(self, angle):
		return angle/self.get_w()
	
	def time2str(self, t):
		return time.strftime('%H:%M:%S', time.gmtime(t))

	def get_sunlight_hours(self, neighborhood_name, building_name, apartment_number):
		init_angle, end_angle = self.get_sunlight_angles(neighborhood_name, building_name, int(apartment_number))
		return "{}-{}".format( self.time2str(self.angle2time(init_angle)+self.get_raise_time()), \
			self.time2str(self.angle2time(end_angle)+self.get_raise_time()) )
