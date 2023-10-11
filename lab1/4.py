def camel_to_snake(input_string):
    output_string = ""
    for i in input_string:
        if i.isupper():
            output_string += "_" + i.lower()
        else:
            output_string += i
    return output_string

input_string = "addClient addChild addEvent Dad"
result = camel_to_snake(input_string)
print ("Snake case: ", result)