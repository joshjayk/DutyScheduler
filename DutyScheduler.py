"""
Takes a file called availability.txt and generates a set of duty days
for each person in the file, keeping track of total duty days of the semester.
"""

from datetime import datetime
import calendar
import random

def main():
	unavailable = {}
	with open('availability.txt') as file:
		#The first two lines are comments made by me that can be
		#skipped over.
		file.readline()
		file.readline()
		#The third and fourth line are the month and year.
		line1 = file.readline()
		month = line1[8:10]
		line2 = file.readline()
		year = line2[7:11]
		#For each line in the file, if it starts with a '#', skip over it.
		#Else, split the line into name, day and count strings, remove new line character
		#from count strings, turn the day strings into a list of days, and format
		#the list of days into datetime format.
		#name = Name of each person.
		#dates = Raw dates listed in the input file.
		#dayCount = Count of how many weekdays they have been on duty.
		#endCount = Count of how many weekends they have been on duty.
		for line in file:
			if line[0] == "#":
				continue
			else:
				name, dates, dayCount, endCount, dayPrim, endPrim = line.split(' : ')
				if '\n' in endCount:
					endCount = endCount[:-1]
				daylist = dates.split()
				datetimelist = []
				for day in daylist:
					day = datetime.strptime(year + '-' + month + '-' + day, '%Y-%m-%d')
					datetimelist.append(day)
				#unavailable = dictionary where key = name, and the value is a list of 3 things:
				#1. The list of formatted datetime days,
				#2. The dayCount for that name,
				#3. The endCOunt for that name.
				unavailable.setdefault(name, [])
				unavailable[name].append(datetimelist)
				unavailable[name].extend((dayCount, endCount, dayPrim, endPrim))
		totaldays = calendar.monthrange(int(year), int(month))[1]
	print(unavailable)
#def createDuty(availability):
	

if __name__ == "__main__":
	main()