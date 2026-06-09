# ============================================
#   Student Grade Calculator
#   By: FazarathAhamed | ICBT Campus CSE
#   GitHub: github.com/FazarathAhamed
# ============================================

import datetime

def get_grade(average):
    if average >= 90:
        return "A+", "Excellent!"
    elif average >= 80:
        return "A", "Very Good!"
    elif average >= 70:
        return "B", "Good!"
    elif average >= 60:
        return "C", "Average"
    elif average >= 50:
        return "D", "Below Average"
    else:
        return "F", "Fail"

def get_gpa(average):
    if average >= 90:
        return 4.0
    elif average >= 80:
        return 3.7
    elif average >= 70:
        return 3.3
    elif average >= 60:
        return 3.0
    elif average >= 50:
        return 2.0
    else:
        return 0.0

def calculate_student():
    print("=" * 50)
    print("     STUDENT GRADE CALCULATOR")
    print("     ICBT Campus | CSE Department")
    print("=" * 50)

    name = input("\nEnter Student Name: ")
    student_id = input("Enter Student ID: ")

    print("\nEnter marks for each subject (0-100):")
    print("-" * 40)

    subjects = {}
    num_subjects = int(input("How many subjects? "))

    for i in range(num_subjects):
        subject = input(f"\nSubject {i+1} name: ")
        while True:
            try:
                mark = float(input(f"Marks for {subject}: "))
                if 0 <= mark <= 100:
                    subjects[subject] = mark
                    break
                else:
                    print("Please enter marks between 0 and 100!")
            except ValueError:
                print("Please enter a valid number!")

    # Calculate results
    total = sum(subjects.values())
    average = total / len(subjects)
    grade, remark = get_grade(average)
    gpa = get_gpa(average)

    # Display Result
    print("\n")
    print("=" * 50)
    print("           RESULT CARD")
    print("=" * 50)
    print(f"  Student Name : {name}")
    print(f"  Student ID   : {student_id}")
    print(f"  Date         : {datetime.date.today()}")
    print("-" * 50)
    print(f"  {'SUBJECT':<20} {'MARKS':>10} {'GRADE':>10}")
    print("-" * 50)

    for subject, mark in subjects.items():
        s_grade, _ = get_grade(mark)
        print(f"  {subject:<20} {mark:>10.1f} {s_grade:>10}")

    print("-" * 50)
    print(f"  {'Total Marks':<20} {total:>10.1f}")
    print(f"  {'Average':<20} {average:>10.2f}")
    print(f"  {'Final Grade':<20} {grade:>10}")
    print(f"  {'GPA':<20} {gpa:>10.1f}")
    print(f"  {'Remark':<20} {remark:>10}")
    print("=" * 50)

    # Pass/Fail summary
    print("\n  SUBJECT WISE ANALYSIS:")
    print("-" * 50)
    passed = 0
    failed = 0
    for subject, mark in subjects.items():
        status = "Pass" if mark >= 50 else "Fail"
        print(f"  {subject:<25} {status}")
        if mark >= 50:
            passed += 1
        else:
            failed += 1

    print("-" * 50)
    print(f"  Passed Subjects : {passed}")
    print(f"  Failed Subjects : {failed}")
    print("=" * 50)

    # Save to file — UTF-8 encoding fixes the emoji/unicode error
    save = input("\nSave result to file? (yes/no): ").lower()
    if save == "yes":
        filename = f"{name.replace(' ', '_')}_result.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("STUDENT GRADE REPORT\n")
            f.write("====================\n")
            f.write(f"Name    : {name}\n")
            f.write(f"ID      : {student_id}\n")
            f.write(f"Date    : {datetime.date.today()}\n\n")
            for subject, mark in subjects.items():
                s_grade, _ = get_grade(mark)
                f.write(f"{subject}: {mark} ({s_grade})\n")
            f.write(f"\nAverage : {average:.2f}\n")
            f.write(f"Grade   : {grade}\n")
            f.write(f"GPA     : {gpa}\n")
            f.write(f"Remark  : {remark}\n")
        print(f"Result saved as '{filename}'")

def main():
    while True:
        calculate_student()
        again = input("\nCalculate for another student? (yes/no): ").lower()
        if again != "yes":
            print("\nThank you! Goodbye!")
            break

if __name__ == "__main__":
    main()