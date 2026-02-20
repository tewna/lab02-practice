#bug tests 
def count_vowels ( text ) :
    vowels = "aeiou"
    count = 0
    for char in text :
        if char in vowels :
            count += 1
    return count

result = count_vowels ("HELLO")
print ( f" Vowel count : { result }")