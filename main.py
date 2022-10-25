print("Personalised Login Console!!!")
print()
print("P.S. this Personalised Login Console is only for Ritwik, Sid and Bugs ")
print()
print("password recognised in lowercase only")
print()
username = input("Type your username: ")
print()
password = input("Type your password: ")
print()
if username == "Ritwik" and password == "ritwik":
  print("Hey there Ritwik! Welcome back!")
elif username == "Sid" and password == "sid":
  print("Long time no see Sid!")
elif username == "Bugs" and password == "bugs":
  print("The return of the mighty Bugs Bunny!!!")
else:
  print("You are someone else and not recognised in our system!")