import unittest
import unittest.mock as mock

import sys
sys.path.append('.')
from sunlight.neighborhood import Neighborhood
from sunlight.building import Building
from sunlight.exceptions.incorrect_desc_exception import MissingKeyException, IncorrectValueException
from sunlight.exceptions.not_in_exception import NotInNeighborhoodException

TEST_NEIGHBORHOOD_NAME = "Neighborhood Test"
TEST_NEIGHBORHOOD_APARTMENTS_HEIGHT = 4

# To test get_eastern/westen_buildings, dif returned values for get_number(). Instead of mocking
# the class Building I'm creating a simplest version
class MockBuilding:
	def __init__(self, name, number):
		self.name = name
		self.number = number

	def get_name(self):
		return self.name

	def get_number(self):
		return self.number

class NeighborhoodTest(unittest.TestCase):

	def setUp(self):
		self.neighborhood = Neighborhood(TEST_NEIGHBORHOOD_NAME, TEST_NEIGHBORHOOD_APARTMENTS_HEIGHT, \
			[MockBuilding(i, i) for i in range(5)])

	def test_get_name(self):
		self.assertEqual(TEST_NEIGHBORHOOD_NAME, 
			self.neighborhood.get_name())

	def test_is_in_neighborhood_ok(self):
		self.assertEqual(True, self.neighborhood.is_in_neighborhood(0))

	def test_is_in_neighborhood_ko(self):
		with self.assertRaises(NotInNeighborhoodException):
			self.neighborhood.is_in_neighborhood(-1)
		with self.assertRaises(NotInNeighborhoodException):
			self.neighborhood.is_in_neighborhood(5)
		with self.assertRaises(NotInNeighborhoodException):
			self.neighborhood.is_in_neighborhood(7)

	def test_get_building_number_ok(self):
		self.assertEqual(0, self.neighborhood.get_building_number(0))

	def test_get_building_number_ko(self):
		with self.assertRaises(NotInNeighborhoodException):
			self.neighborhood.get_building_number(7)

	def test_get_eastern_buildings(self):
		self.assertEqual(1, len(self.neighborhood.get_eastern_buildings(1)))
	
	def test_get_western_buildings(self):
		self.assertEqual(3, len(self.neighborhood.get_western_buildings(1)))

if __name__ == '__main__':
    unittest.main()