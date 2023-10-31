#2 liste si face reuniune a-b si b-a si intersectie 
def pb1(a,b):
    intersection = list(set(a).intersection(set(b)))
    union = list(set(a).union(set(b)))
    a_minus_b = list(set(a) - set(b))
    b_minus_a = list(set(b) - set(a))
    return intersection, union, a_minus_b, b_minus_a

#un dictionar in care tin minte de cate ori apare fiecare caracter
def pb2(text):
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

#functie care primeste 2 dictionare si verifica daca sunt egale
def pb3(dict1, dict2):
    # Check if the keys are the same
    if set(dict1.keys()) != set(dict2.keys()):
        return False
    
    for key in dict1.keys():
        value1 = dict1[key]
        value2 = dict2[key]
        
        # If the value is a dictionary, recursively compare the dictionaries
        if isinstance(value1, dict) and isinstance(value2, dict):
            if not compare_dicts(value1, value2):
                return False
        # If the value is a list or set, convert to tuple and compare
        elif isinstance(value1, (list, set)) and isinstance(value2, (list, set)):
            if tuple(value1) != tuple(value2):
                return False
        # Otherwise, compare the values directly
        elif value1 != value2:
            return False
    
    return True


#functie care primeste un tag si un continut si returneaza un string de forma <tag>continut</tag>
def pb4(tag, content, **kwargs):
    attributes = ""
    for key, value in kwargs.items():
        attributes += f' {key}="{value}"'
    return f'<{tag}{attributes}>{content}</{tag}>'

#functie care primeste un dictionar si o lista de tuple si verifica daca dictionarul respecta regulile
def pb5(rules, d):
    for key, prefix, middle, suffix in rules:
        if key not in d:
            return False
        value = d[key]
        if not value.startswith(prefix):
            return False
        if middle not in value[1:-1]:
            return False
        if not value.endswith(suffix):
            return False
    return True

#functie care primeste o lista si returneaza un tuplu cu numarul de elemente unice si numarul de elemente duplicate
def pb6(lst):
    unique = len(set(lst))
    duplicates = len(lst) - unique
    return (unique, duplicates)

#functie care primeste un numar variabil de seturi si returneaza un dictionar cu operatiile de reuniune, intersectie si diferenta
def pb7(*sets):
    operations = {}
    for i in range(len(sets)):
        for j in range(i+1, len(sets)):
            set1 = sets[i]
            set2 = sets[j]
            key1 = f"{set1} | {set2}"
            key2 = f"{set1} & {set2}"
            key3 = f"{set1} - {set2}"
            key4 = f"{set2} - {set1}"
            operations[key1] = set1.union(set2)
            operations[key2] = set1.intersection(set2)
            operations[key3] = set1.difference(set2)
            operations[key4] = set2.difference(set1)
    return operations

#functie care primeste un dictionar si returneaza o lista cu cheile prin care se poate ajunge la o anumita valoare
def pb8(mapping: dict) -> list:
    visited = set()
    result = []
    current_key = "start"
    while current_key not in visited:
        visited.add(current_key)
        result.append(mapping[current_key])
        current_key = mapping[current_key]
    return result[:-1]

#functie care primeste un numar variabil de argumente si un numar variabil de keyword arguments si returneaza numarul de argumente care se gasesc si in argumente si in keyword arguments
def pb9(*args, **kwargs):
    count = 0
    for arg in args:
        if arg in kwargs.values():
            count += 1
    return count

def main():
    print("pb1")
    list_a = [1, 2, 3, 4, 5]
    list_b = [3, 4, 5, 6, 7]
    result = pb1(list_a, list_b)
    print("Intersection:", result[0])
    print("Union:", result[1])
    print("a - b:", result[2])
    print("b - a:", result[3])
    print("end pb1\n")

    print("pb2")
    text = "This is a test"
    result = pb2(text)
    print(result)
    print("end pb2\n")

    print("pb3")
    dict1 = {"a": 1, "b": 2, "c": 3}
    dict2 = {"a": 1, "b": 2, "c": 3}
    dict3 = {"a": 1, "b": 2, "c": 4}
    print(pb3(dict1, dict2))
    print(pb3(dict1, dict3))
    print("end pb3\n")

    print("pb4")
    print(pb4("a", "Hello there", href="http://python.org", _class="my-link"))
    print("end pb4\n")

    print("pb5")
    rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
    d = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
    result = pb5(rules, d)
    print(result)
    print("end pb5\n")

    print("pb6")
    lst = [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 8, 8, 9]
    unique, duplicates = pb6(lst)
    print(f"List: {lst}")
    print(f"Number of unique elements: {unique}")
    print(f"Number of duplicate elements: {duplicates}")
    print("end pb6\n")

    print("pb7")
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}
    result = pb7(set1, set2)
    print(result)
    print("end pb7\n")

    print("pb8")
    print(pb8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
    print("end pb8\n")

    print("pb9")
    print(pb9(1, 2, 3, 4, x=1, y=2, z=3, w=5))
    print("end pb9\n")
    
main()

