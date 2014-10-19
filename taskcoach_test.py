#!/usr/bin/python3

# Program                : taskcoach_test.py
# Version                : 0.3.1
# Created by             : petervdb
# Last updated by        : petervdb
# Creation date          : 29/09/2014
# Last updated           : 19/10/2014
# Test Taskcoach version : 1.4.1
#
# You can use this script to analyse a Taskcoach tsk file
#
# ToDo
# Create subroutine to be able to go recursively into sub-tasks
#

from sys import argv
from os.path import exists
import xml.etree.ElementTree as etree
import getopt
import json

def print_categories():
	# find all categories
	allcategories = root.findall('category')
	print ("Let's display all categories:")
	print(allcategories)
	print("-----------------------------------------------------------------------------------")

def print_tasks():
	# find all tasks
	alltasks =  root.findall('task')
	print ("Let's display all tasks:")
	print(alltasks)
	print("-----------------------------------------------------------------------------------")

def check_taskcoach_file():
	# Quit if file does not exist
	if exists(taskfile):
		tk_file = etree.parse(taskfile)
		return(tk_file)
	else:
		print("Sorry, %s does not exist." % taskfile)
		exit(1)

def parse_taskcoach_file(root):
	count = 0
	tasks = 0
	cats = 0
	for child in root:
		# Display Element information
		# print(child)
		# Display content
		print(root[count].attrib)
		
		# cur_text is a JSON string
		cur_text = root[count].attrib
		
		# A need the tag to figure out what I need to do with the JSON string
		cur_tag = root[count].tag
		# only works for tasks and categories
		if cur_tag == "task":
			tasks = tasks + 1
			subject = cur_text['subject']
			print("Task %s : %s " % (tasks, subject))
		if cur_tag == "category":
			cats = cats + 1
			subject = cur_text['subject']
			print("Category %s : %s " % (cats, subject))
		print("Child elements of %s: %s " % (subject, len(root[count])))
		if len(root[count]) > 0:
			parse_child_object(count,subject)
		print("-----------------------------------------------------------------------------------")
		count = count + 1

def parse_child_object(count,subject):
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
	print("Will analyze child objects for %s." % subject)
	count2 = 0
	for child2 in root[count]:
		print(root[count][count2].attrib)
		count2 = count2 + 1

# This is a test program to analyze taskcoach files
print("This is a small program to analyse your Taskcoach file")

# The script requires the Taskcoach file as argument
# Quit if usage is not good
try:
	script, taskfile = argv
except getopt.GetoptError:
	print("Usage: %s <toachcoach_file.tsk>" % script)
	exit(2)

tk_file = check_taskcoach_file()

root = tk_file.getroot()
print("Document root: %s " % root)
print("Child elements of root: %s " % len(root))

parse_taskcoach_file(root)

# print_tasks()
# print_categories()

