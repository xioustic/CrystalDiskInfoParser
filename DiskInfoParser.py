"""
by Xioustic

Reads data from DiskInfo[x64].exe output and spits out
JSON. Launch DiskInfo[x64].exe, go to Edit, make sure
everything under Copy Option is checked. Then go to Edit
and click Copy. Then paste into input.txt. Run this script
and it will spit out output.json.
"""

from enum import Enum

class ReadMode(Enum):
	start = 1
	controllers = 2
	disklist = 3
	drivedata = 4
	smartdata = 5
	identifydata = 6
	smartreaddata = 7
	smartreadthreshold = 8

current_mode = ReadMode.start
input_data = None

with open('input.txt','r') as f:
	input_data = f.read()

for linenum, line in enumerate(input_data.splitlines()):
	print linenum, line