# if
# elif
# else


age = int(input("Please enter your age:"))
print(type(age))

if age < 21:
    print("You can not smoke.")
elif age == 21:
    print("You are now 21, you can smoke.")
elif age == 100:
    print("You are 100 years old, quit smoking.")
else:
    print("You can smoke.")
