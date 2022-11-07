#!/usr/bin/env python3.7

#Python implementation goes here

value = int(input("Enter an Integer value: "))

if value % 5 == 0 and value % 2 == 0:
    print("FizzBuzz")
elif value % 3 == 0:
    print("Fizz")
elif value % 5 == 0:
    print("Buzz")
else:    
    print(value)