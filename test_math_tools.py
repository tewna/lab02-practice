#checker mathtools 

from math_tools import add, multiply, is_even, subtract, max_of_three, is_palindrome, find_min, remove_duplicates

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    print("test_add: ALL PASSED")

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0
    print("test_multiply: ALL PASSED")

def test_is_even():
    assert is_even(4) == True
    assert is_even(7) == False
    assert is_even(0) == True
    print("test_is_even: ALL PASSED")

def test_subtract():
    assert subtract(2,4) == -2   #minus ans
    assert subtract(0,-1) == 1  #sign change 
    assert subtract(796,3) == 793
    print("test_subtract: ALL PASSED")

def test_max_of_three():
    assert max_of_three(2,2,5) == 5
    assert max_of_three(3,3,3) == 3
    assert max_of_three(-4, 0,-9) == 0
    assert max_of_three(54.6,6,9) == 54.6
    assert max_of_three(-5,-5,9) == 9
    print("test_max_of_three: ALL PASSED")

def test_is_palindrome():
    assert is_palindrome('hello') == False
    assert is_palindrome('racecar') == True
    assert is_palindrome('racecar mom civic') == False
    assert is_palindrome('Racecar mom civic') == False
    assert is_palindrome('') == True
    assert is_palindrome("RaCeCAR") == False
    print("test_is_palindrome: ALL PASSED")

def test_find_min():
    assert find_min([0,23,-3]) == -3
    assert find_min([4,2,4,7,4,1]) == 1
    assert find_min([-2,-5,2]) == -5
    print("test_find_min: ALL PASSED")

def test_remove_duplicates():
    assert remove_duplicates(['s','a','s','a','t','c','x']) == ['s','a','t','c','x']
    assert remove_duplicates([1,2,2,3]) == [1,2,3]
    assert remove_duplicates([3,1,2,1]) == [3,1,2]
    assert remove_duplicates([5,5,5]) == [5]
    assert remove_duplicates([]) == []
    assert remove_duplicates(["a","b","a"]) == ["a","b"]
    print("test_remove_duplicates = ALL PASSED")


# Run all tests
test_add()
test_multiply()
test_is_even()
test_subtract()
test_max_of_three()
test_is_palindrome()
test_find_min()
test_remove_duplicates()
print("--- All tests passed! ---")
