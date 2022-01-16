# Top Process Parser
# Made in VSC on Ubuntu Focal Fossa :)
# By Lior 
# December 2021

import csv
import json
import operator


class TopProcessParser:

	# function for dumping file to json
	def make_json(csvFilePath, jsonFilePath):
		# complexity: O(n)

		# create a dictionary
		data = {}
		
		# Open a csv reader called DictReader
		with open(csvFilePath, encoding='utf-8') as csvf:
			csvReader = csv.DictReader(csvf)
			
			# Convert each row into a dictionary
			# and add it to data
			for rows in csvReader:
				
				# Assuming a column named 'PID' to
				# be the primary key
				key = rows['PID']
				data[key] = rows

		# Open a json writer, and use the json.dumps()
		# function to dump data to a precreated json file
		with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
			jsonf.write(json.dumps(data, indent=4))
		
		return data
			
	# function for printing all users
	def print_users(data):
		# complexity: O(n)
		
		# create a list
		users = []
		
		# store all data dict users in users list 
		for process in data:
			users.append(data[process]['USER'])

		# remove duplicates from users list
		users = list(dict.fromkeys(users))

		# print users list
		print(users)
	
	# function for printing all commands of a user (provide user name)
	def print_user_commands(data, user):
		# complexity: O(n log n)
		
		# check for wrong input
		if type(user) != str:
			print("wrong input, string expected")
		
		# create a list
		user_commands = []

		# store all data dict commands that run by defined user
		for process in data:
			if data[process]['USER'] == user:
				user_commands.append(data[process]['COMMAND'])

		# print user commands
		print(user_commands)
	
	# function for getting command name by pid
	def pid_command_name(data, pid):
		# complexity: O(1)
		
		# check for wrong input
		if type(int(pid)) != int:
			print("wrong input, int in a string expected")

		print(data[pid]['COMMAND'])
	
	# function for printing top 5 commands sorted by cpu usage
	def top_5_CPU_commands(data):
		# complexity: O(n)

		# create a dictionary
		cpu_usage = {}

		# store cpu usage, converted to float, per PID
		for process in data:
			cpu_usage[process] = float(data[process]['%CPU'])

		# sorting cpu usage dict by cpu usage, saving only top 5 processes	
		cpu_usage = dict(sorted(cpu_usage.items(), key=operator.itemgetter(1),reverse=True)[:5])

		# printing top 5 processes		
		for cpu in cpu_usage:
			print(data[cpu]['COMMAND'])


# Define file paths 
csvFilePath = r'top_linux.csv'
jsonFilePath = r'top_linux.json'

# Call the make_json function and store it in a dict var for future use
data = TopProcessParser.make_json(csvFilePath, jsonFilePath)

TopProcessParser.print_users(data)

TopProcessParser.print_user_commands(data, 'root')

TopProcessParser.pid_command_name(data, '9')

TopProcessParser.top_5_CPU_commands(data)

