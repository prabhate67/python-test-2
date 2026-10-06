#Q8. Read a temperature in Celsius as a decimal number. Convert it to Fahrenheit (C x 9 / 5 + 32) and to Kelvin (C + 273). Print both, then the types of celsius and fahrenheit.
c=float(input("Enter the temp in Celsius:"))
print("Fahrenheit=", (c*9/5+32))
print("Kelvin=", (c+273))