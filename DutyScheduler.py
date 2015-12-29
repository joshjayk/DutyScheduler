"""
Takes a file called availability.txt and generates a set of duty days
for each person in the file, keeping track of total duty days of the semester.
"""

from datetime import datetime

def main():
	unavailable = {}
	with open('availability.txt') as file:
		# The first two lines are comments made by me that can be
		# skipped over.
		file.readline()
		file.readline()
		# The third and fourth line are the month and year.
		line1 = file.readline()
		month = line1[7:9]
		line2 = file.readline()
		year = line2[6:10]
		# For each line in the file, if it starts with a '#', skip over it.
		# Else, split the line into a name and day string, remove new line character
		# from day strings, turn the day strings into a list of days, and format
		# the list of days into datetime format.
		for line in file:
			if line[0] == "#":
				continue
			else:
				name, dates = line.split(': ')
				if '\n' in dates:
					dates = dates[:-1]
				daylist = dates.split()
				datetimelist = []
				for day in daylist:
					day = datetime.strptime(year + '-' + month + '-' + day, '%Y-%m-%d')
					datetimelist.append(day)
				# Lastly, put the appropriate datetime formatted list into the dictionary
				# with its respective name.
				unavailable[name] = datetimelist
		print(unavailable)

if __name__ == "__main__":
	main()