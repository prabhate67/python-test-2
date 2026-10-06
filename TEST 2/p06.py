#Q6. Read an integer. Store whether it is even in a variable called is_even, then print the variable and its type.

a=int(input("Enter your number:"))
if a%2==0:
   print("true")
elif a%2!=0:
   print("false")