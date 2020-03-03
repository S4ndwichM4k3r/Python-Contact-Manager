
firstNames = []
lastNames = []
phoneNumbers = []
emailAddresses = []

inputFile = open("Contacts1.txt","r")

contacts = inputFile.readlines()

for i in range (len(contacts)):
	parts = contacts[i].split(";")
	firstNames.append(parts[0].strip())
	lastNames.append(parts[1].strip())
	phoneNumbers.append(parts[2].strip())
	emailAddresses.append(parts[3].strip())

menuOption = "0"

while menuOption != "5":

	print("1. Add a new contact\n2. Print all contacts\n3. Delete a contact\n4. Search for contact\n5. Save and Exit")
	
	menuOption = input()
	
	if menuOption == "1":
		firstNames.append(input("what's the first name?"))
		lastNames.append(input("what's the last name?"))
		phoneNumbers.append(input("what's the phone number?"))
		emailAddresses.append(input("what's the email address?"))
		
	elif menuOption == "2":
		print ("\n\n")
		for i in range(len(firstNames)):
			print(str(i+1) + ".")
			print("  " + firstNames[i] + " " + lastNames[i])
			print("    " + phoneNumbers[i])
			print("    " + emailAddresses[i] + "\n")
		
	elif menuOption == "3":
		print("you chose three")	
		
	elif menuOption == "4":
		print("please enter last name to search for")
		lastName = input()
outputFile = open("contacts1.txt","w")
		
#prints out the contacts with the semicolons and such
for i in range(len(firstNames)):
	outputFile.write(firstNames[i] + ";" + lastNames[i] + ";" + phoneNumbers[i] + ";" + emailAddresses[i] + "\n")
outputFile.close()
		
		