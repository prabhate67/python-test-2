principal = int(input())
rate = int(input())
time = int(input())

interest = principal * rate * time / 100
amount = principal + interest

print("Interest:", interest)
print("Amount:", amount)
print(type(principal), type(interest))