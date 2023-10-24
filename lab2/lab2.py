from collections import Counter

#o lista cu n elemente din sirul lui fibonacci
def pb1(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence[:n]

#functie care verifica daca un nr e prim
def is_prime(number):
    if number<=1:
        return False
    if number<=3:
        return True
    
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    i = 5
    while i*i <= number:
        if number % i or number % (i+2) == 0:
            return False
        i+=6
    
    return True

#o lista cu numerele prime din alta lista primita ca parametru
def pb2(numbers):
    prime_numbers = []
    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers



#o functie care primeste 2 liste de numere si calucleaza intersectia , reuniunea , a-b si b-a
def pb3(a,b):
    intersection = list(set(a).intersection(set(b)))
    union = list(set(a).union(set(b)))
    a_minus_b = list(set(a) - set(b))
    b_minus_a = list(set(b) - set(a))
    return intersection, union, a_minus_b, b_minus_a

#o lista cu notele muzicale si o lista cu mutarile si pozitia de start
def pb4(notes, moves, start_position):
    song_length = len(notes)
    composed_song = []
    composed_song.append(notes[start_position])
    for move in moves:
        start_position = (start_position + move) % song_length
        composed_song.append(notes[start_position])

    return composed_song

#modifica o matrice astfel incat elementele de dedesubtul diagonalei principale sa fie 0
def pb5(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if i > j:
                matrix[i][j] = 0

    return matrix

#o functie care primeste un nr x si o lista de liste si returneaza elementele care apar de x ori in lista
def pb6(x, *lists):
    # Concatenate all the input lists into a single list
    all_items = [item for sublist in lists for item in sublist]

    # Count the occurrences of each item
    item_counts = Counter(all_items)

    # Filter items that appear exactly x times
    result = [item for item, count in item_counts.items() if count == x]

    return result


def is_palindrome(n):
    return str(n) == str(n)[::-1]

def pb7(numbers):
    palindromes = [n for n in numbers if is_palindrome(n)]
    return (len(palindromes), max(palindromes))


def pb8(x=1, strings=[], flag=True):
    result_lists = []

    for string in strings:
        ascii_list = []

        for char in string:
            ascii_code = ord(char)
            if (ascii_code % x == 0 and flag) or (ascii_code % x != 0 and not flag):
                ascii_list.append(char)

        result_lists.append(ascii_list)

    return result_lists

def pb9(matrix):
    blocked_seats = []

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            height = matrix[row][col]
            can_see_game = True

            # Check if there is a taller spectator in front (above or on the same row)
            for r in range(row):
                if matrix[r][col] >= height:
                    can_see_game = False
                    break

            if not can_see_game:
                blocked_seats.append((row, col))
    return blocked_seats

def pb10(*args):
    # Use the zip function to combine elements from each list
    combined = list(zip(*args))
    return combined

def pb11(tuples):
    return sorted(tuples, key=lambda x: x[1][2])
    # x[1] este al doilea element din tuplu, x[1][2] este al treilea caracter din al doilea element din tupla

def pb12(words):
    rhyme_dict = {}

    for word in words:
        # Get the last two letters of the word
        rhyme = word[-2:]

        # Add the word to the corresponding rhyme group
        if rhyme in rhyme_dict:
            rhyme_dict[rhyme].append(word)
        else:
            rhyme_dict[rhyme] = [word]

    # Convert the dictionary values to a list
    grouped_words = list(rhyme_dict.values())

    return grouped_words

def main():
        print("pb1")
        result=pb1(10)
        print(result)
        print("end pb1\n")

        print("pb2")
        result=pb2([1,2,3,4,5,6,7,8,9,10])
        print(result)
        print("end pb2\n")

        print("pb3")
        list_a = [1, 2, 3, 4, 5]
        list_b = [3, 4, 5, 6, 7]

        result = pb3(list_a, list_b)

        print("Intersection:", result[0])
        print("Union:", result[1])
        print("a - b:", result[2])
        print("b - a:", result[3])
        print("end pb3\n")

        print("pb4")
        musical_notes = ["do", "re", "mi", "fa", "sol"]
        moves = [1, -3, 4, 2]
        start_position = 2
        result = pb4(musical_notes, moves, start_position)
        print(result)
        print("end pb4\n")


        print("pb5")
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        result = pb5(matrix)
        for row in result:
            print(row)
        print("end pb5\n")

        print("pb6")
        result = pb6(2,[1,2,3], [2,3,4],[4,5,6], [4,1, "test"])
        print(result)
        print("end pb6\n")

        print("pb7")
        result = pb7([123, 121, 444, 22, 12321, 12345, 123321])
        print(result)
        print("end pb7\n")

        print("pb8")
        result = pb8(2, ["test", "hello", "lab002"], flag=False)            
        print(result)
        print("end pb8\n")

        print("pb9")
        matrix =   [[1, 2, 3, 2, 1, 1],

                    [2, 4, 4, 3, 7, 2],

                    [5, 5, 2, 5, 6, 4],

                    [6, 6, 7, 6, 7, 5]]
        result = pb9(matrix)
        print(result)
        print("end pb9\n")

        print("pb10")
        result = pb10([1,2,3], [5,6,7], ["a", "b", "c"])
        print(result)
        print("end pb10\n")

        print("pb11")
        result = pb11([('abc', 'bcd'), ('abc', 'zza')])
        print(result)
        print("end pb11\n")

        print("pb12")
        result =['ana', 'banana', 'carte', 'arme', 'parte']
        print(result)
        print("end pb12\n")
main()
