names  = ['Abilash','Rajan',"Naruto","Ram"]

for index in range(len(names)):
    if len(names[index]) > 5:
        print(names[index])
    if 'n' in names[index] or 'N' in names[index]:
        print(names[index] + " has N/n char")

while len(names) > 0:
    names.pop()

print(names)