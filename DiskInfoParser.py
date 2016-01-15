"""
by Xioustic (https://github.com/xioustic/)

Uses DiskInfo.exe to create DiskInfo.txt data, then reads
that in and spits out JSON.
"""

import subprocess
import enum
import re
import json

class ReadMode(enum.Enum):
  start = 1
  controllermap = 2
  disklist = 3
  drivedata = 4
  smartdata = 5
  identifydata = 6
  smartreaddata = 7
  smartreadthreshold = 8


# generate data
print "Running DiskInfo.exe"
try:
  status = subprocess.call("DiskInfo.exe /CopyExit")
except WindowsError, e:
  if "Error 740" in str(e):
    raise Exception("This program must be run as an administrator.")
  else:
    raise e

if status != 0:
  raise Exception("DiskInfo.exe exited with status code "+status)


# read data
input_data = None

with open('DiskInfo.txt','r') as f:
  input_data = f.read()

input_data = input_data.decode('utf-16')


# parse data
obj = {"controllers_disks": {}, "disks": []}
curmode = ReadMode.start
curdiskname = None
curdiskidx = None
curcontroller = None

for linenum, line in enumerate(input_data.splitlines()):

  # skip blank lines
  if len(line) == 0:
    #print "blank",line
    continue

  # mode pivots
  if re.search("^-- Controller Map",line):
    curmode = ReadMode.controllermap
    continue

  if re.search("^-- Disk List",line):
    curmode = ReadMode.disklist
    continue

  if re.search("^-- S.M.A.R.T. ",line):
    curmode = ReadMode.smartdata
    continue

  if re.search("^-- IDENTIFY_DEVICE ",line):
    curmode = ReadMode.identifydata
    continue

  if re.search("^-- SMART_READ_DATA ",line):
    curmode = ReadMode.smartreaddata
    continue

  if re.search("^-- SMART_READ_THRESHOLD ",line):
    curmode = ReadMode.smartreadthreshold
    continue

  if curmode == ReadMode.controllermap:
    if line.startswith(" + "):
      curcontroller = line[len(" + "):]
      obj["controllers_disks"][curcontroller] = []
    if line.startswith("   - "):
      obj["controllers_disks"][curcontroller].append(line[len("   - "):])
    continue

  if curmode == ReadMode.disklist:
    result = re.search("^ \((\d+)\) (.*) : (.*) \[.*$",line)
    if result:
      idx, name, size = result.groups()
      obj['disks'].append({"idx": idx, "name": name, "size": size})
    elif line.startswith("-----------------"):
      curmode = ReadMode.drivedata
    continue

  result = re.search("^ \((\d+)\) (.*)$",line)
  if result:
    curmode = ReadMode.drivedata
    curdiskidx, curdiskname = result.groups()
    continue

  if curmode == ReadMode.drivedata:
    splitstrip = [x.strip() for x in line.split(" : ")]
    if len(splitstrip) > 1:
      attribute, value = splitstrip
    continue



# output data
print json.dumps(obj, indent=2, separators=(",", ": "))