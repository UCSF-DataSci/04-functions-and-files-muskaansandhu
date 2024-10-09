#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""
#IMPORTING BY FIBONNACI GENERATING FUNCTION FROM PROBLEM 1 AND ARGPARSE 
import fibonnaci
import argparse


#DEFINING FUNCTION TO CHECK IF IT IS PRIME  
def prime_function(number): 
    if number <=1: 
        return False
    for i in range(2, int(number ** 0.5) + 1): #checking up to the square root of the number 
        if number % i == 0:
        	return False
    return True

#DEFINING FUNCTION TO TEST THE LARGEST PRIME NUMBER FROM FIBONNACI SEQUENCE 
def prime_fibonnaci(num):
     fib_sequence = fibonnaci.fibonacci_sequence(num)
     fib_prime = filter(prime_function, fib_sequence)
     answer = max(fib_prime)
     return answer 

#USING ARGPARSE TO SPECIFY UPPER LIMIT AND OUTPUT FILE NAME FOR COMMAND LINE ARGUMENTS 
parser = argparse.ArgumentParser()
parser.add_argument("limit", type=int, help="Upper limit for Fibonacci number") #defining limit 
args = parser.parse_args() 

if __name__ == "__main__":
    result = prime_fibonnaci(args.limit)
    print(result)

#After running the code, the answer is 28657. 