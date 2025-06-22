#question 1
name = input("Enter student name: ")
student_class = input("Enter class: ")

marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

total_marks = sum(marks)
per = (total_marks / 500) * 100  # Assuming each subject is out of 100

print("\n----- Student Result -----")
print(f"Name       : {name}")
print(f"Class      : {student_class}")
print(f"Percentage : {per:.2f}%")

#quetion 2
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
combined = string1 + string2

print(f"Concatenated String     : {combined}")
print(f"Length                  : {len(combined)}")
print(f"Uppercase               : {combined.upper()}")
print(f"Lowercase               : {combined.lower()}")
print(f"Title Case              : {combined.title()}")
print(f"Swap Case               : {combined.swapcase()}")
print(f"Is Alphabetic           : {combined.isalpha()}")
print(f"Starts with '{string1}' : {combined.startswith(string1)}")
print(f"Ends with '{string2}'   : {combined.endswith(string2)}")
print(f"Count of 'a'            : {combined.count('a')}")
print(f"Replace 'a' with '@'    : {combined.replace('a', '@')}")
print(f"Reverse String          : {combined[::-1]}")
