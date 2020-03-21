# *args
# def add(num1, num2, num3):
#     print(num1 + num2 + num3)
#
#
# # add(1, 1)
# add(1, 1, 4)
def add(*args):
    print(args)
    print(type(args))
    print(sum(args))
    for i in args:
        print('i love', i)


add(1, 1)
add(12, 56, 32, 66, 33)
