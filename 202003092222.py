# "字典"

my_dic = {"key": "value", "key1": "value1"}

myPhones = {"Iphone": 1000, "Sumsang 59": 900}
print(myPhones)

Iphone_Price = myPhones["Iphone"]
print("Iphone_Price " + str(Iphone_Price))

# change key value
myPhones["Iphone"] = 500
print("Iphone_Price " + str(myPhones["Iphone"]))

myPhones.clear()
print(myPhones)
