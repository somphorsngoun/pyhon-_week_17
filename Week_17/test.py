def sum(array):
    sum = 0
    for n in array:
        sum += n
    return sum

def createNewArray(array, value):
    return array.append(value)

def getAvg(array):
    return int(sum(array) / len(array))

numbers = [10, 5, 7, 8, 6]
evenList = []
for n in numbers:
    if n%2 != 1:
        createNewArray(evenList, n)
print(getAvg(evenList))