#buggyfirstn 
def first_n(items, n):
    result = []
    for i in range(1, n):
        result.append(items[i])
    return result

print(first_n([10, 20, 30, 40], 3))
# Expected: [10, 20, 30]
# Actual:   [20, 30]

def test_first_n():
	assert first_n([24,6,31,45], 2) == [24,6]  #this will do it
     
print(test_first_n())