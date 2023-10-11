def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for i in input_string:
        if i in vowels:
            count += 1
    return count

input_string = "Salutare! Bine ai venit la curs la Python"

result = count_vowels(input_string)

print ("Number of vowels: ", result)