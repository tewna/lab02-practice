#bughunt3 
def remove_negatives(numbers):
    newlist = []
    for num in numbers:
        if num > 0:
            newlist.append(num)
    return newlist

print(remove_negatives([1, -2, -3, 4, -5]))
# Expected: [1, 4]
# Actual:   [1, -3, 4]