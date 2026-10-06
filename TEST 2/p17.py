age = int(input())
marks = float(input())
id_card = input()

age_ok = age >= 18 and age <= 25
marks_ok = marks >= 60
id_ok = id_card == "yes"

eligible = age_ok and marks_ok and id_ok

print("Age ok:", age_ok)
print("Marks ok:", marks_ok)
print("Eligible:", eligible)