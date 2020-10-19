import unittest
import unittest.mock as mock
import math

import sys
sys.path.append('.')

from sunlight.shadow import Shadow

class MockBuilding:
	def get_height(self):
		return 10
	def get_distance(self):
		return 10


class ShadowTest(unittest.TestCase):
	@mock.patch('sunlight.building.Building')
	def setUp(self, mock_building):
		mock_building.return_value = MockBuilding()
		self.shadow = Shadow(mock_building())

	def test_compte_length(self):
		alpha = math.pi / 4
		self.assertEqual(10 / math.tan(alpha), self.shadow.compute_length(alpha))

	def test_compute_intersection_angle(self):

		# Sun raising, (xp,yp) western than the building

		# Higher point, no intersection -> 0
		xp, yp = 15, 15
		self.assertEqual(0.0, self.shadow.compute_intersection_angle(xp, yp)) 

		# Same height, no intersection
		xp,yp = 15, 10
		self.assertEqual(0.0, self.shadow.compute_intersection_angle(xp, yp))

		# Shorther, intersection
		xp, yp = 15, 5
		self.assertEqual(math.pi/4, self.shadow.compute_intersection_angle(xp,yp))

		# The sun is setting, (xp,yp) eastern than the building

		# Higher point, no intersection -> PI
		xp, yp = 5, 15
		self.assertEqual(math.pi, self.shadow.compute_intersection_angle(xp,yp))

		# Same height, no intersection
		xp,yp = 5, 10
		self.assertEqual(math.pi, self.shadow.compute_intersection_angle(xp, yp))

		# Shorther, intersection
		xp, yp = 5, 5
		self.assertEqual(3*math.pi/4, self.shadow.compute_intersection_angle(xp,yp))


if __name__ == '__main__':
    unittest.main()