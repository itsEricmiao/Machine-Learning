newItems = []
items.sort()
for j in range(len(items)-1):
    i = j+1
    times = 0;
    for i in range (len(items)):
        if(items[i] == items[j]):
            times = times + 1
    newItems.append(items[i])
    newItems.append(times)

print(newItems)