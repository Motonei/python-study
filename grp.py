# A bank is reviewing loan applications. Create a program that checks salary and age. Applicants below 21 years should be rejected, while those above 21 with salaries above KES 50,000 should be approved.
age = int(input("Age: "))
salary = int(input("Salary: "))

if age < 21:
    print("Rejected")
else:
    if salary > 50000:
        print("Approved")
    else:
        print("Rejected")
# Q2
# A smartphone company wants a battery safety alert. Build a program that checks battery percentage. If below 20%, warn the user to charge. If below 5%, activate emergency mode.
battery=float(input("Enter battery percentage:  "))

if battery<5:
    print("Emergency Mode Activated!")
elif battery<20:
    print("Warning: Battery low. Please charge your device.")
else:
    print("Battery level is sufficient.")
# Q3
# A school wants to monitor attendance. Create a system that stores attended classes and total classes, calculates attendance percentage, and warns students whose attendance is below 75%.
attended = int(input("Enter the number of classes attended: "))
total = int(input("Enter total number of classes: "))

percentage = (attended / total) * 100

if percentage < 75:
    print("Warning: Attendance below 75%")
else:
    print("Attendance is satisfactory")

# Q4
# A courier company wants to improve communication. Build a system that compares expected delivery date with the current day and alerts customers if the package is delayed.
expected=input("Enter the expected day of delivery:  ")

today="04/26/2026"

if expected>today:
    print("Package on its way")
elif expected==today:
    print("Delivery on time")
else:
    print("Package delayed")

