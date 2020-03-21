# 列表解析式

a = [i * 2 for i in range(0, 11)]
print(a)

my_list = ['xiao ming', 'wang er', 'zhang san', 'wang si']
wang_list = [name for name in my_list if name.startswith('wang')]
print(wang_list)
