# "元组"
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

# print(type(my_list))
# print(type(my_tuple))
# print(len(my_list))
# print(len(my_tuple))
# print(my_list[0])
# print(my_tuple[0])

print(dir(my_list))
print('===============')
print(dir(my_tuple))

# list is mutable
# tup is inmutable

my_list.remove(2)
print(my_list)
# fault example
# my_tuple.remove(2)
# print(my_tuple)
