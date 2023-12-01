import sys

for word in sys.stdin:
    first_digit = 0
    last_digit = 0
    for char in word:
        if char.isdigit():
            first_digit = char
            break
    print('first digit', first_digit)
    
    for char in reversed(word):
        if char.isdigit():
            last_digit = char
            break
    print('last digit', last_digit)
    
    number = str(first_digit) + str(last_digit)
    print('number', number)

    number_to_add = int(number)
    sum_of_numbers = sum_of_numbers + number_to_add
    print("sum =", sum_of_numbers)
    print()
  
