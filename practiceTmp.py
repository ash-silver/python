cro=['c=', 'c-']
word=input()

for i in range(len(cro)):
    a = word.replace(cro[i], "a")
print(a)