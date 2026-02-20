#buggytax 
def total_with_tax(price, tax_rate):
    tax = price * tax_rate
    total = price + tax
    return total    #fixed

print(total_with_tax(100, 0.15))
# Expected: 115.0
# Actual:   None