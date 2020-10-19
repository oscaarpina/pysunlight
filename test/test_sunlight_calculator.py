import unittest
import unittest.mock as mock
import json
import math

import sys
sys.path.append('.')
from sunlight.sunlight_calculator import SunlightCalculator

class SunlightCalculatorTest(unittest.TestCase):

	def setUp(self):
		self.calculator = SunlightCalculator()
		self.s = """[ 
		{"neighborhood":"N1", 
		"apartments_height":2, 
		"buildings" : [
			{"name":"N1_B1", "apartments_count":2, "distance":0},
			{"name":"N1_B2", "apartments_count":4, "distance":4},
			{"name":"N1_B3", "apartments_count":2, "distance":8}
		]},
		{"neighborhood":"N2", 
		"apartments_height":3, 
		"buildings" : [
			{"name":"N2_B1", "apartments_count":4, "distance":0},
			{"name":"N2_B2", "apartments_count":2, "distance":20},
			{"name":"N2_B3", "apartments_count":4, "distance":40}
		]}
		]"""
		self.d = json.loads(self.s)

	def test_init(self):
		self.calculator.init(self.s)

		for n in self.d:
			for b in n["buildings"]:
				for a in range(b["apartments_count"]):
					self.assertEqual(a, self.calculator.city.get_apartment(n["neighborhood"], b["name"], a).get_number())

	def test_compute_sunlight_angles(self):
		self.calculator.init(self.s)

		# start angles of eastern buildings
		self.assertEqual(0.0, self.calculator.get_sunlight_angles("N1", "N1_B1", 0)[0])
		self.assertEqual(0.0, self.calculator.get_sunlight_angles("N2", "N2_B1", 3)[0])

		# end angles of westen buildings 
		self.assertEqual(math.pi, self.calculator.get_sunlight_angles("N1", "N1_B3", 0)[1])
		self.assertEqual(math.pi, self.calculator.get_sunlight_angles("N2", "N2_B3", 0)[1])

		# N1 -> 2 - 4 - 2
		self.assertEqual(math.pi/4, self.calculator.get_sunlight_angles("N1","N1_B2", 0)[0])
		self.assertEqual(True,      self.calculator.get_sunlight_angles("N1","N1_B2", 1)[0] - math.atan(0.5) < 1e-5)
		self.assertEqual(0.0,       self.calculator.get_sunlight_angles("N1","N1_B2", 2)[0])

	def test_get_sunlight_hours(self):
		self.calculator.init(self.s)
		self.assertEqual("10:31:45-15:07:15", self.calculator.get_sunlight_hours("N1","N1_B2", 0))


if __name__ == '__main__':
    unittest.main()