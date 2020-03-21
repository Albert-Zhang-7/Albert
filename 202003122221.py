file = open("Albert.txt")
text = file.read()
print(text)
file.close()

# 不用close
with open("Albert.txt") as f:
    print(f.read())
# w是覆盖写，a是追加（append）
with open("Albert.txt", 'a') as f:
    f.write('I love you.\n')

with open("Albert.txt") as f:
    print(f.read())

print(help(open))
