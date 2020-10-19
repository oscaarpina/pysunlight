from sunlight.sunlight_calculator import SunlightCalculator

s = """[ 
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
c = SunlightCalculator()
c.init(s)

print("N1 - N1_B2 - 0", c.get_sunlight_hours("N1", "N1_B2", 0))
print("N1 - N1_B2 - 1", c.get_sunlight_hours("N1", "N1_B2", 1))
print("N1 - N1_B2 - 2", c.get_sunlight_hours("N1", "N1_B2", 2))
