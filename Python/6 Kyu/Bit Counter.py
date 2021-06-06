# In response to: https://www.codewars.com/kata/526571aae218b8ee490006f4

def count_bits(n):
    bits=0
    while (n > 0):
        if (not(n % 2 == 0)):
            bits +=1
        n= int(n/2)
    return bits
