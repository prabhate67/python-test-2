#Read two values from the user and swap them using a third variable. Print the type of x before the swap, then print both values after it.
a=int(input("enter your number:"))
b=int(input("enter your number:"))
c= b,a=a,b
print("after swap:", a,b)
print(type(a))