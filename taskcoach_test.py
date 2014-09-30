#!/usr/bin/python3

# Program                : taskcoach_test.py
# Version                : 0.2.0
# Created by             : petervdb
# Last updated by        : petervdb
# Creation date          : 29/09/2014
# Last updated           : 30/09/2014
# Test Taskcoach version : 1.4.1
#
# You can use this script to analyse a Taskcoach tsk file
#
# ToDo
#

from sys import argv
from os.path import exists
import xml.etree.ElementTree as etree
import getopt
import json

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
	
	# cur_text is a JSON string
	cur_text = root[count].attrib
	
	# A need the tag to figure out what I need to do with the JSON string
	cur_tag = root[count].tag
	# only works for tasks and categories
	if cur_tag == "task":
		subject = cur_text['subject']
		print("Task : %s " % subject)
	if cur_tag == "category":
		subject = cur_text['subject']
		print("Category : %s " % subject)
	print("Child elements of %s: %s " % (subject, len(root[count])))
	print("-----------------------------------------------------------------------------------")
	count = count + 1
# find all tasks
alltasks =  root.findall('task')
print ("Let's display all tasks:")
print(alltasks)
print("-----------------------------------------------------------------------------------")

# find all categories
allcategories = root.findall('category')
print ("Let's display all categories:")
print(allcategories)
print("-----------------------------------------------------------------------------------")
