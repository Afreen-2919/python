d={}
name=input("Enter Student Name:")
n=int(input("Enter Number of Subjects:"))
for i in range(n):
    subject=input("Enter Subject Name:")
    mark=float(input(f"Enter mark in {subject}"))
    d[subject]=mark

total=0
highest=-1
lowest=101
for subject,mark in d.items():
    total+=mark
    if mark>highest:
        highest=mark
        highest_subject=subject
    if mark<lowest:
            lowest=mark
            lowest_subject=subject
percentage=total/n
if percentage >= 90: 
    grade = "A+" 
    performance = "Outstanding" 
elif percentage >= 80: 
    grade = "A" 
    performance = "Excellent" 
elif percentage >= 70: 
    grade = "B" 
    performance = "Very Good"
elif percentage >= 60: 
    grade = "C" 
    performance = "Good" 
elif percentage >= 50: 
    grade = "D" 
    performance = "Average" 
else: 
    grade = "F" 
    performance = "Needs Improvement" 
print("\n--- Academic Performance ---") 
print("Student Name :", name) 
print("Total Marks  :", total) 
print("Percentage   :", round(percentage, 2), "%") 
print("Grade        :", grade) 
print("Performance  :", performance)
print(f"Highest Mark: {highest_subject}-{highest}")
print(f"Lowest Mark:{lowest_subject}-{lowest}")
print(f"Comment:Concentrate More on:{lowest_subject}")


'''

sample output

Enter Student Name:Anu
Enter Number of Subjects:5
Enter Subject Name:English
Enter mark in English95
Enter Subject Name:Maths
Enter mark in Maths96
Enter Subject Name:Physics
Enter mark in Physics81
Enter Subject Name:Chemistry
Enter mark in Chemistry98
Enter Subject Name:Computer
Enter mark in Computer99

--- Academic Performance ---
Student Name : Anu
Total Marks  : 469.0
Percentage   : 93.8 %
Grade        : A+
Performance  : Outstanding
Highest Mark: Computer-99.0
Lowest Mark:Physics-81.0
Comment:Concentrate More on:Physics

'''
            