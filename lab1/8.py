def count_bits_1(number):
    count = 0
    
    while number > 0:
        if number & 1:
            count += 1
        
        number >>= 1
    
    return count

nb = 30
result = count_bits_1(nb)
print(f"Numarul de 1 din reprezentarea binara a nr: {nb} este: {result}")
