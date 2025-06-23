#
# #ques1
# n1 = int(input("Enter First number :"))
# n2 = int(input("Enter second number :"))
# opr = input("Enter operator (+,-,*,/) :")
# if opr == "+":
#     result = n1 + n2
# elif opr == "-":
#     result = n1-n2
# elif opr == "*":
#     result = n1*n2
# else:
#     result = n1/n2
#
# print("Result is : ",result)

#ques2
num = int(input("Enter a number:"))
n1 = num
reverse = 0
while num>0:
    digit = num%10
    reverse = reverse*10 + digit
    num = num//10

if n1 == reverse:
    print("no. is palindrome")
else:
    print("not palindrome")