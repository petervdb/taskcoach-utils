#!/usr/bin/python3

from sys import argv
from os.path import exists
import xml.etree.ElementTree as etree
import getopt

# This is a test program to analyze taskcoach files
print("This is a small program to analyse your Taskcoach file")

# The script requires the Taskcoach file as argument
# Quit if usage is not good
try:
	script, taskfile = argv
except getopt.GetoptError:
	print("Usage: %s <toachcoach_file.tsk>" % script)
	exit(2)

# Quit if file does not exist
if exists(taskfile):
	tk_file = etree.parse(taskfile)
else:
	print("Sorry, %s does not exist." % taskfile)
	exit(1)

root = tk_file.getroot()
print("Document root: %s " % root)
print("Child elements of root: %s " % len(root))
count = 0
for child in root:
	print(child)
	print(root[count].attrib)
	print("-----------------------------------------------------------------------------------")
	count = count + 1
