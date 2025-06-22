"""marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

total_marks = sum(marks)
per = (total_marks / 500) * 100  # Assuming each subject is out of 100


print(f"Percentage : {per:.2f}%")

if per > 60 :
    print("grade A")
elif per > 50:
    print("grade B")
elif per > 40:
    print("grade C")
else :
    print("Fail")
"""
#
# n1 = int(input("Enter a numer :"))
# fact = 1
# if n1<0:
#     print("factorial does not exist")
# elif n1 == 0:
#     print("factorial of 0 is 1")
# else:
#     for i in range(1,n1+1):
#         fact *= i
#     print(f"factorial of {n1} is {fact} ")

# l = [10,30,2,39,18,26]
# n= len(l)
# #finding smallest no.
# l.sort()
# print(f"smallest no. is {l[0]}")
# print(f" Second smallest no. is {l[1]}")
# print(f"Second largest no. is {l[n-2]}")

items = []
prices = []

while True:
    print('''
    ---- Billing Menu ----
    1. Create Bill (Add Items)
    2. Display Items with Price and Total
    3. Display Total Amount
    4. Exit
    ''')

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item = input("Enter item name: ")
        price = float(input("Enter item price: ₹"))
        items.append(item)
        prices.append(price)
        print(f"Added: {item} - ₹{price:.2f}")

    elif choice == '2':
        if not items:
            print("No items in the bill.")
        else:
            print("\n--- Bill Details ---")
            total = 0
            for i in range(len(items)):
                print(f"{items[i]} - ₹{prices[i]:.2f}")
                total += prices[i]
            print(f"\nTotal Amount: ₹{total:.2f}")

    elif choice == '3':
        total = sum(prices)
        print(f"\nTotal Amount: ₹{total:.2f}")

    elif choice == '4':
        print("Exiting the billing program. Thank you!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")


