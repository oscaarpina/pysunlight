import unittest
import unittest.mock as mock

import sys
sys.path.append('.')

from sunlight.city import City
from sunlight.exceptions.not_in_exception import NotInCityException


class MockNeighborhood:
	def __init__(self, name):
		self.name = name
	def get_name(self):
		return self.name

class CityTest(unittest.TestCase):

	def setUp(self):
		self.city = City([MockNeighborhood(i) for i in range(5)])

	def test_is_in_city_ok(self):
		self.assertEqual(True, self.city.is_in_city(0))
		self.assertEqual(True, self.city.is_in_city(1))
		self.assertEqual(True, self.city.is_in_city(2))
		self.assertEqual(True, self.city.is_in_city(3))
		self.assertEqual(True, self.city.is_in_city(4))

	def test_is_in_city_ko(self):
		with self.assertRaises(NotInCityException):
			self.city.is_in_city(-1)
		with self.assertRaises(NotInCityException):
			self.city.is_in_city(5)
if __name__ == '__main__':
    unittest.main()