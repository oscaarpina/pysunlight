import sys
import os
import json
from sunlight.sunlight_calculator import SunlightCalculator

args = sys.argv
assert len(args)==5, "You have to specify 4 arguments: 1-file 2-neighborhood 3-building 4-apartment"
assert args[1].endswith(".txt") or args[1].endswith(".json"), "The file must be .txt or .json."
assert os.path.isfile(args[1]), "The file does not exist."

with open(args[1], "r") as f:
	s = f.read()

c = SunlightCalculator()
c.init(s)

print("Sunlight hours of {} - building {} - apartment {}:".format(args[2], args[3], args[4]))
print(c.get_sunlight_hours(args[2], args[3], args[4]))