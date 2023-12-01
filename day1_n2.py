import sys

sum_of_numbers = 0

numbers_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9"

}

all_numbers = list(numbers_dict.keys())

# print("o", "spongebob".find("b", 7))
# print("bob", "spongebob".find("bob"))

for word in sys.stdin:
    first_position_kept = None
    first_number_kept = None
    
    last_position_kept = None
    last_number_kept = None
    for number in all_numbers:
        position = word.find(number)
        if not (position == -1):
            if first_position_kept is None or position < first_position_kept:
                first_position_kept = position
                first_number_kept = number
            if last_position_kept is None or position > last_position_kept:
                last_position_kept = position
                last_number_kept = number
                
    number = numbers_dict[first_number_kept]+numbers_dict[last_number_kept]
    print(numbers_dict[first_number_kept]+numbers_dict[last_number_kept])

    print('number', number)

    number_to_add = int(number)
    sum_of_numbers = sum_of_numbers + number_to_add
    print("sum =", sum_of_numbers)
    print()
