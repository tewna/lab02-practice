#buggyrev 
def reverse_list(items):
    for i in range(len(items)//2 ): #Hypothesize, thinking itis double reversing cause it goes over it more, limited it so it doesnt go past half point
        j = len(items) - 1 - i
        items[i], items[j] = items[j], items[i] #Isolate, the bug here was that it was reversing it and then going over again and re-reversing it
    return items

print(reverse_list([1, 2, 3, 4, 5]))
# Expected: [5, 4, 3, 2, 1]
# Actual:   [1, 2, 3, 4, 5]

def test_reverse_list():
    assert reverse_list([1,2,3,4,5]) == [5,4,3,2,1] #catches it, Reproducing the bug, Test after changing it to //2

test_reverse_list() #Verify as it runs