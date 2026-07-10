#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    if roman_string == "":
        return 0
    roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }
    total = 0
    for i, char in enumerate(roman_string):
        if char not in roman_values:
            return 0
        current_value = roman_values[char]
        next_value = (roman_values[roman_string[i + 1]] 
                      if i + 1 < len(roman_string) else 0)
        if current_value < next_value:
            total -= current_value
        else:
            total += current_value
    return total
