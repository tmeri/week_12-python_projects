#!/usr/bin/env python3.7

import random #Importing the Random module which will generate numbers based on a range provided by the developer/programmer

def ec2_name_chars(num_chars): #definition of function that the value assigned to num_char to generate several characters
return “”.join(chr(random.randint(33,125)) for i in range(num_chars)) #Takes all items in an iterable and joins then into one string

ec2_count = int(input(“Enter the number of AWS EC2 instances “)) # Counter that will be incremented through each iteration

#List of authorized departments who may utilize this name generating script, also those are the recognized department names to be entered by the user

depts = [“Accounting”, “FinOps”, “Marketing”]
count = 0 # Counter used to determine the number of requested random names enter by the user

while count != ec2_count: # Counter that will be incremented through each iteration
if count < ec2_count:
print(“Please select from one of these departments: Accounting, FinOps or Marketing”)
ec2_name = str(input(“\nTo be included in the name of your new AWS ec2 instance: “)) #Prompts the user for the desired named of the ec2 instance
if ec2_name in depts:
print(ec2_name + ec2_name_chars(15)) #Print statement presents both the requested name and the generated characters
print(“\n”)
count += 1
elif not ec2_name in depts: # The user did not enter the correct spelling or upper case character(s)
ec2_name = str(input(“\nPlease try again, please select from one of these departments: Accounting, FinOps or Marketing!\n”))
if ec2_name in depts: # Check to see if the new entry is correct
print(ec2_name + ec2_name_chars(15)) #Print statement presents both the requested name and the generated characters
count += 1
else:
print(“\nYou are not authorized to use this program!”) # User still didn’t enter the correct name so they are told they are not authorized
print(“\nPlease obtain the required authorization and rerun the program once again, Thank You!”)
break
# Notifies the user that their request has been completed
print(‘\nYour request has been completed and ‘ + str(count) + ‘ randomly generated name(s) were created!’)
print(‘Thank you!’)