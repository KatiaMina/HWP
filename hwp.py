"""Let's do work!"""

from datetime import date, timedelta, datetime
from astrophy.table import Table, Column
import numpy as np 

d = datetime(1,1,1,1,1,1)
User = "Katia"
File = open_file("HWP", mode="w", title = "Data")
group = File.create_group("/", User, "Log Tables")

##################
#Creating Classes#
##################

class Event(object):
#List of days, numeric time#
	days = ['SU', 'M', 'T', 'W', 'TH', 'F', 'SA']
	times = [-1, -1, -1, -1, -1]

	def __init__(self, datetime):
		self.days=days
		self.times = [time]
		while len(days) > len(self.times):
			self.times.append(time)

class Lecture(Event):
#List of Days, 24-hour number as time#
	
	def __init__(self, days=None, time=None, Discussion=None):
		if days:
			self.days=days
		if time:
			self.times = [time]
		while len(days) > len(self.times):
			self.times.append(time)
		self.discussion = Discussion

	def change_time(self,new_time):
		#new_time is number#

		if new_time != self.times[0]:
			self.times = [new_time]
		while len(self.days) > len(self.times):
			self.times.append(new_time)

	def change_days(self, new_days):
		#list of new_days#

		self.days = new_days
		while len(new_days) > len(self.times):
			self.times.append[self.times[0]]
		while len (new_days) < len(self.times):
			self.times = self.times[0:-1]

class Discussion(Event):

	def __init__(self, days, time):
		self.days=days
		self.times = [time]
		while len(days) > len(self.times):
			self.times.append(time)

	def change_time(self, new_time):
		#new_time is number#

		if new_time != self.times[0]:
			self.times = [new_time]
		while len(self.days) > len(self.times):
			self.times.append(new_time)

	def change_days(self, new_days):
		#list of new_days#

		self.days = new_days
		if len(new_days) > len(self.times):
			self.times.append[self.times[0]]
		elif len (new_days) < len(self.times):
			self.times = self.times[0:2]


class Class(object):
#Class Subject, Class Lecture, Class Discussion#

	assignments = []

	def __init__(self, name, Lecture, Subject=None):
		self.name = name
		self.subject = Subject
		self.lecture = Lecture
		self.discussion = Lecture.discussion
		

	def add_lecture(self, Lecture):
		self.lecture = Lecture

	def change_lecture(self, Lecture):
		if self.lecture == None:
			return "You have not added a lecture yet"
		else:
			self.lecture = Lecture

	def add_discussion(self, Discussion):
		self.discussion = Discussion

	def change_discussion(self, Discussion):
		if self.discussion == None:
			return "You have not added a discussion yet"
		else:
			self.discussion = Discussion

	def add_assignment(self, Assignment):
		#Takes Class Assignment#
		self.assignments.append(Assignment)

	def __repr__(self):
		return self.name

	def __str__(self):
		return self.name

class Subject(object):
	#Takes list of types of assignments (strings)#
	assign_types = []

	def __init__(self, assign_types=None):
		self.assign_types = assign_types

	def add_assignment_type(self, new_type):
		if new_type in self.assign_types:
			assert False, '{0} is already an assignment type for the {1} class'.format(new_type, self)
		else:
			self.assign_tyes.append(new_type)
			assert '{0} is now an assignment type for the {1} class'.format(new_type, self)


######################
#Creating Assignments#
######################

class Log(IsDescription):
	#Assignment is the datetime that the assignment was created
	assignment = StringCol(26)
	timestamp = StringCol(26)
	comp_done = Int8Col()
	time_total = Int8Col()
	time_per_comp = Int16Col()

def add_entry(Assignment, comp_done, time_total):
	entry = Assignment.log.row
	entry['assignment'] = Assignment
	entry['timstamp'] = d.today().__str__()
	entry['comp_done'] = comp_done
	entry['time_total'] = time_total
	entry['time_per_comp'] = comp_done/time_total
	entry.append()
	Assignment.log.flush()
		
class Assignment(object):
	#Unique datetime created
	created = d.now()
	#Number of components
	components = 0
	#Number of components left
	compleft = 0
	#Time per components
	timepercomp = 0
	#Predicted time per component
	ptimepercomp = 0
	#Name of Components
	component_name = "component"
	components_name = "components"

	def __init__(self, Class, due_date, components=None, timepercomp=None, component_name = None):
		#class Class
		self.cls = Class
		self.cls.assignments.append(self)
		#Datetime due_dates
		self.due_date = due_date
		self.days_until_due = date.today() - due_date
		if components:
			self.components = components
			self.compleft = components
		if timepercomp:
			self.timepercomp = timepercomp
		if component_name:
			self.component_name = component_name
			self.components_name = component_name + "s"
		#Make log
		self.log = File.create_table(group, str(self.cls), Log,created.__str__() + " Work Log")

	def work_on(self, components_done, time):
		if self.compleft == 0:
			assert "This assignment is completed!"
		elif self.components==0:
			return "Add {0} to this assignment to work on it".format(self.components_name)
		else:
			print("Good job!")
			self.compleft = self.compleft - components_done
			self.log.add_entry(self, components_done, time)
			if self.compleft !=1:
				return "You now have {0} {1} left in this assignment".format(self.compleft, self.components_name)
			else:
				return "You now have {0} {1} left in this assignment".format(self.compleft, self.component_name)

	def __repr__(self):
			return self.created.__str__()

	#def recalculate(self):
Stat135 = Class("Stat135")
disc135 = Discussion(['T', 'TH'], time(15))
lect135 = Lecture(['T', 'TH'], time(17), disc135)
Stat135.add_lecture(lect135)
math1 = Assignment(Stat135, date(2017,7,30), 50, 2, "problem")




