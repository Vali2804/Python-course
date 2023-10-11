def count_occurrences(input_string, search_string):
    count = 0
    for i in range(len(input_string)):
        if input_string[i:i+len(search_string)] == search_string:
            count += 1
    return count

string1 = "ana are multe mere. cate mere are ana?"
string2 = "ana"

result = count_occurrences(string1, string2)
print ("Number of occurrences: ", result)
