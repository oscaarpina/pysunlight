import unittest
import sys
sys.path.append('.')

from sunlight.building import Building
from sunlight.exceptions.incorrect_desc_exception import MissingKeyException, IncorrectValueException
from sunlight.exceptions.not_in_exception import NotInBuildingException

TEST_BUILDING_NAME = "Building Test"
TEST_BUILDING_APARTMENTS_COUNT = 5
TEST_BUILDING_DISTANCE = 20
TEST_BUILDING_NUMBER   = 2
TEST_APARTMENTS_HEIGHT = 5

TEST_BUILDING_DESCRIPTION = {
	Building.B_NAME_KEY : TEST_BUILDING_NAME,
	Building.B_APARTMENTS_COUNT_KEY : TEST_BUILDING_APARTMENTS_COUNT,
	Building.B_DISTANCE_KEY : TEST_BUILDING_DISTANCE
}

class BuildingTest(unittest.TestCase):
	def setUp(self):
		self.building = Building(TEST_BUILDING_NAME, TEST_BUILDING_APARTMENTS_COUNT, \
			TEST_BUILDING_DISTANCE, TEST_APARTMENTS_HEIGHT)

	def test_get_name(self):
		self.assertEqual(TEST_BUILDING_DESCRIPTION["name"], self.building.get_name())

	def test_get_distance(self):
		self.assertEqual(TEST_BUILDING_DESCRIPTION["distance"], self.building.get_distance())

	def test_get_apartments_count(self):
		self.assertEqual(TEST_BUILDING_DESCRIPTION["apartments_count"], self.building.get_apartments_count())

	def test_get_apartments_height(self):
		self.assertEqual(TEST_APARTMENTS_HEIGHT, self.building.get_apartments_height())

	def test_get_height(self):
		self.assertEqual(TEST_BUILDING_DESCRIPTION["apartments_count"] * TEST_APARTMENTS_HEIGHT, self.building.get_height())

	def test_get_shadow(self):
		pass

	def test_is_description_correct_ok(self):
		self.assertEqual(True, Building.is_description_correct(TEST_BUILDING_DESCRIPTION))

	def test_is_description_correct_ko(self):
		with self.assertRaises(MissingKeyException):
			Building.is_description_correct({})
		with self.assertRaises(MissingKeyException):
			Building.is_description_correct({Building.B_NAME_KEY:"Test", Building.B_APARTMENTS_COUNT_KEY:4})
		with self.assertRaises(MissingKeyException):
			Building.is_description_correct({Building.B_NAME_KEY:"Test", Building.B_DISTANCE_KEY:20})
		with self.assertRaises(MissingKeyException):
			Building.is_description_correct({Building.B_DISTANCE_KEY:20, Building.B_APARTMENTS_COUNT_KEY:4})
		with self.assertRaises(IncorrectValueException):
			Building.is_description_correct({Building.B_NAME_KEY:"Test", Building.B_APARTMENTS_COUNT_KEY:-4, Building.B_DISTANCE_KEY:20})
		with self.assertRaises(IncorrectValueException):
			Building.is_description_correct({Building.B_NAME_KEY:"Test", Building.B_APARTMENTS_COUNT_KEY:4, Building.B_DISTANCE_KEY:-20})

	def test_is_in_building_ok(self):
		self.assertEqual(True, self.building.is_in_building(3))

	def test_is_in_building_ko(self):
		with self.assertRaises(NotInBuildingException):
			self.building.is_in_building(-1)
		with self.assertRaises(NotInBuildingException):
			self.building.is_in_building(5)
		with self.assertRaises(NotInBuildingException):
			self.building.is_in_building(7)

	def tearDown(self):
		pass

if __name__ == '__main__':
    unittest.main()