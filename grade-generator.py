#!/usr/bin/python3
import csv 
import sys
"""Grade Generator Script"""
#This is grade generator created by KALIZA SABRINA. It will help calculating grades.
def validation():
    """Prompts and validates user input for one assignment. Returns a tuple."""
    
    # Assignment name
    while True:
        assignment_name = input("Enter the Assignment name: ").strip()
        if assignment_name:
            break
        print("Invalid assignment name. Please enter a non-empty string.")

    # Category
    while True:
        category = input("Enter the category of the assignment (FA/SA): ").upper()
        if category in ['FA', 'SA']:
            break
        print("Invalid category. Please enter 'FA' or 'SA'.")

     # Grade
    while True:
        try:
            grade = float(input("Enter the grade (0-100): "))
            if 0 <= grade <= 100:
                break
            print("Grade must be between 0 and 100.")
        except ValueError:
            print("Please enter a numeric grade.")
    # Weight
    while True:
        try:
            weight = int(input("Enter the weight of the assignment: "))
            if weight > 0:
                break
            print("Weight must be a positive integer.")
        except ValueError:
            print("Please enter an integer for weight.")

    return assignment_name, category, grade, weight


def calculation_logic(category, grade, weight, FA, SA, assignment_name):
    """Calculates and updates FA/SA values."""
    weighted_grade = weight * (grade / 100)

    if category == 'FA':
        FA += weighted_grade
    else:
        SA += weighted_grade

    total_grade = FA + SA
    gpa = (total_grade / 100) * 5.0

    FA_pass = 60 * 0.5
    SA_pass = 40 * 0.5

    print("\n... RESULTS ...")
    print(f"Total Formative: {FA:.2f} / 60")
    print(f"Total Summative: {SA:.2f} / 40")
    print(f"-------------------------")
    print(f"Total Grade:     {total_grade:.2f} / 100")
    print(f"GPA:             {gpa:.4f}")

    if FA >= FA_pass and SA >= SA_pass:
        print("Status:          PASS")
    else:
        print("Status:          FAIL")
        print(f"Resubmission:    {assignment_name}")

    return FA, SA


def export_to_csv(assignments, filename="grades.csv"):
    """Exports all assignment data to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Assignment Name", "Category", "Grade", "Weight"])
        for assignment in assignments:
            writer.writerow(assignment)

    print(f"\nGrades exported to {filename}")


def main():
    assignments = []
    FA = 0
    SA = 0

    while True:
        assignment_data = validation()  # get validated user input
        assignments.append(assignment_data)

        name, category, grade, weight = assignment_data
        FA, SA = calculation_logic(category, grade, weight, FA, SA, name)

        cont = input("\nDo you want to add another assignment? (y/n): ").lower()
        if cont != 'y':
            break

    export_to_csv(assignments)


if __name__ == "__main__":
    main()


