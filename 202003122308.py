# **kwargs
def m1(*args, **kwargs):
    print(type(args))
    print(type(kwargs))


dic_albert = {'name': 'albert', 'age': 18, 'height': 180, 'weight': 140}


def someone(dic_someone):
    for k, v in dic_someone.items():
        print(k, ':', v)


someone(dic_albert)


def someone(**kwargs):
    for k, v in kwargs.items():
        print(k, ':', v)


someone(name='xiaoming', age=18, height=180)
