# condition = 1
# while condition < 10:
#     print("hello while loop")
#     condition = condition + 1

while True:
    a = int(input("Please enter number a: "))
    b = int(input("Please enter number b: "))
    c = a + b
    print("The result is %s" % c)
    if c == 100:
        break
