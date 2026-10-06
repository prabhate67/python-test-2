price = float(input())
tax_percent = float(input())

tax = price * tax_percent / 100
total = price + tax

print("Tax:", tax)
print("Total:", total)