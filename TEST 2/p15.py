username = input()
pin = int(input())

username_ok = username == "admin"
pin_ok = pin == 1234

access = username_ok and pin_ok

print("Username ok:", username_ok)
print("PIN ok:", pin_ok)
print("Access granted:", access)