#!/usr/bin/python3
import csv
import sys

"""Grade Generator Script"""
# Created by KALIZA SABRINA

def validation():
    """Prompts and validates user input for one assignment. Returns a tuple."""
    
    
    # 1. Assignment Name
    while True:
        assignment_name = input("Enter Assignment Name: ").strip()
        if assignment_name:
            break
        print("name cannot be empty.")

    # 2. Category
    while True:
        category = input("Ente the category(FA/SA): ").strip().upper()
        if category in ['FA', 'SA']:
            break
        print("The category must be 'FA'  or 'SA' .")

    # 3. Grade
    while True:
        try:
            grade = float(input("Enter the grades(0-100): "))
            if 0 <= grade <= 100:
                break
            print("grade must be between 0 and 100.")
        except ValueError:
            print("grade must be a valid number.")

    # 4. Weight
    while True:
        try:
            weight = int(input("Enter the weight: "))
            if weight > 0:
                break
            print("weight must be a positive integer.")
        except ValueError:
            print("weight must be a valid number.")

    return assignment_name, category, grade, weight


def calculation_logic(category, grade, weight, FA, SA):
    """Calculates and updates FA/SA values."""
    weighted_grade = weight * (grade / 100)

    if category == 'FA':
        FA += weighted_grade
    else:
        SA += weighted_grade
    
    return FA, SA


def export_to_csv(assignments, filename="grades.csv"):
    """Exports all assignment data to a CSV file."""
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Assignment", "Category", "Grade", "Weight"])
            for assignment in assignments:
                # assignment is a tuple: (name, cat, grade, weight)
                writer.writerow(assignment)
        print(f"\nGrades exported to {filename}")
    except Exception as e:
        print(f"Oops: Error exporting file: {e}")


def main():
    
    print("\n=== Grade Generator ===\n")
    assignments = []
    FA = 0
    SA = 0
    FA_weight_total = 0
    SA_weight_total = 0

    # --- INPUT LOOP ---
    while True:
        # Get validated user input
        data = validation() 
        assignments.append(data)

        name, category, grade, weight = data
        
        # Track weights for accurate passing logic
        if category == 'FA':
            FA_weight_total += weight
        else:
            SA_weight_total += weight

        # Update score totals
        FA, SA = calculation_logic(category, grade, weight, FA, SA)
        

        dev = input("\nAdd another assignment? (y/n): ").strip().lower()
        if dev not in ['y', 'Y']:
            break

    if not assignments:
        print("\nNo assignments entered. Exiting.")
        sys.exit(0)

    # --- FINAL CALCULATIONS ---
    total_grade = FA + SA
    
    # GPA Calculation: (Total Grade / 100) * 5.0
    gpa = (total_grade / 100) * 5.0

    # Pass/Fail Logic: Must have >= 50% of the points in BOTH categories
    FA_pass = FA >= 30
    SA_pass = SA >= 20
    
    if FA_pass and SA_pass:
        status = "PASS"
    else:
        status = "FAIL"

    # Resubmission Logic

    if status == "PASS":
        # If PASS, check for any assignment with grade < 50
        
        # Iterate through assignments and check if grade (index 2) is < 50
        low_scoring_assignments = [a for a in assignments if a[2] < 50]
        
        if low_scoring_assignments:
            worst = min(low_scoring_assignments, key=lambda x: x[2])
            result = worst[0]
        else:
            result = ["None"]

    else: ## If FAIL, list the WORST assignment from each failed category
        resubmit = []
        if not FA_pass:
            fa_items = [a for a in assignments if a[1] == 'FA']
            if fa_items:
                worst = min(fa_items, key=lambda x: x[2]) 
                resubmit.append(worst[0])
        
        if not SA_pass:
            sa_items = [a for a in assignments if a[1] == 'SA']
            if sa_items:
                worst = min(sa_items, key=lambda x: x[2])
                # Only append if not already added (in case both categories fail and worst is the same assignment)
                if worst[0] not in resubmit:
                    resubmit.append(worst[0])
    
        result = ", ".join(resubmit)

    # --- OUTPUT ---
    print("\n--- RESULTS ---")
    print(f"Total Formative:  {FA:.2f} / 60")
    print(f"Total Summative:  {SA:.2f} / 40")
    print("----------------------")
    print(f"Total Grade:      {total_grade:.2f} / 100")
    print(f"GPA:              {gpa:.4f}")
    print(f"Status:           {status}")

    print(f"Resubmission:     {result}")
    
    print("\n")
    export_to_csv(assignments)

if __name__ == "__main__":
     main()