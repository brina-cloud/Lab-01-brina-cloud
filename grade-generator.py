#!/usr/bin/python3
import csv 
import sys
def validation():
    """Prompts and validates user input for one assignment. Returns a tuple."""
    
    # Assignment name
    while True:
        assignment_name = input("Enter the Assignment name: ").strip()
        if assignment_name:
            break
        print("Invalid assignment name. Please enter a non-empty string.")
