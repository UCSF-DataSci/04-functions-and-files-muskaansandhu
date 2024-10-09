#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""
import argparse

#DEFINING FIBONACCI SEQUENCE FUNCTION
def fibonacci_sequence(limit):
	fib_numbers = [] #generating empty list to store the Fibonacci numbers 
	first_num = 0 #initializing first number of sequence 
	second_num = 1 #initializing second number of sequence 
	while first_num < limit: #making sure that the numbers are less than upper limit 
		fib_numbers.append(first_num) #adding Fibonacci numbers to the list 
		fib_sums = first_num + second_num #adding Fibonacci numbers together 
		first_num = second_num #moving to next Fibonacci number 
		second_num = fib_sums #moving to next Fibonacci number 
	return fib_numbers #returning list 

#USING ARGPARSE TO SPECIFY UPPER LIMIT AND OUTPUT FILE NAME FOR COMMAND LINE ARGUMENTS 
parser = argparse.ArgumentParser()
parser.add_argument("limit", type=int, help="Upper limit for Fibonacci sequence") #defining limit 
parser.add_argument("filename", type=str, help="Output file name") #defining output file name 
args = parser.parse_args()  

if __name__ == "__main__":
    result = fibonacci_sequence(args.limit)  
    try:
        with open(args.filename, 'w') as file:  
            for number in result:  
                file.write(f"{number}\n")  
        print(f"Fibonacci numbers written to {args.filename}") 
    except IOError as error:
        print(f"Error writing to file: {error}")  




