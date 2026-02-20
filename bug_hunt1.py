#bughunt1 
def get_last_three(items):
    start = len(items) - 3
    return items[start:]

print(get_last_three([10, 20, 30, 40, 50]))
# Expected: [30, 40, 50]
# Actual:   [30, 40]
