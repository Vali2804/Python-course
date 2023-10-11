def is_palindrome(number):
    number_str = str(number)
    reversed_str = number_str[::-1]
    return number_str == reversed_str


nb = 1212
if is_palindrome(nb):
    print(nb,"is palindrome")
else:
    print(nb,"isn't palindrome")
