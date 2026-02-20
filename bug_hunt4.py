#bughunt4 
def sum_evens(numbers):
    total = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            total += numbers[i]
    return total

print(sum_evens([1, 2, 3, 4, 5, 6]))
# Expected: 12 (2 + 4 + 6)
# Actual:   9

def first_n ( items , n ) :
    result = []
    for i in range (0 , n) :
        result.append ( items [ i ])  #its gonna miss the 0th item
    return result

print(first_n([24,6,31,45], 2))
