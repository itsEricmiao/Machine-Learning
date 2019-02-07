temp = ['Hello', 'Hi', 'By']
temp_dict = {'Hello:': 1, 'Hi:': 1, 'By:': 1}
print(temp_dict.__len__())







newList = []
for i in range(len(items)-1):
    j = i + 1
    for j in range(len(items)):
        if(items[i] == items[j]):
            if items[i] in newList:
                pass # do nothing
            else:
                newList.append(items[i])
print(newList)
