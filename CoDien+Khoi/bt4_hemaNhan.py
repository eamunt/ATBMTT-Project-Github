'''def char2number(s):
    a = {'A' : 0,
        'B' : 1,
        'C' : 2,
        'D' : 3,
        'E' : 4,
        'F' : 5,
        'G' : 6,
        'H' : 7,
        'I' : 8,
        'J' : 9,
        'K' : 10,
        'L' : 11,
        'M' : 12,
        'N' : 13,
        'O' : 14,
        'P' : 15,
        'Q' : 16,
        'R' : 17,
        'S' : 18,
        'T' : 19,
        'U' : 20,
        'V' : 21,
        'W' : 22,
        'X' : 23,
        'Y' : 24,
        'Z' : 25}


    return a[s]'''


def mod_inverse(x,m): # nghịch đảo của 7
    for n in range(m):
        if (x * n) % m == 1:
            return n
            break
        elif n == m - 1:
            return "Null"
        else:
            continue

def char2number(s):
    if s.isupper():
        a = ord(s)%65
    else:
        a = ord(s)%97
    return a

def number2char_upper(n):
    return chr(n+65)

def number2char_lower(n):
    return chr(n+97)   

#mã hóa
def encode(text , k):
    e_text = ''
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            e_text += number2char_upper( (char2number(char)*k  ) % 26 )
            #C = P*k (mod 26)
        elif char.islower():
            e_text += number2char_lower( (char2number(char)*k  ) % 26 )
        elif char == "":
            e_text+="" #skip
        else:
            e_text += char #special char
    return e_text


#giải mã
def decode(e_text, k):
    d_text = ''
    kn = mod_inverse(k,26)
    for i in range(len(e_text)):
        char = e_text[i]
        if char.isupper():
            d_text += number2char_upper( (char2number(char)*kn ) % 26 )
            #P = C*k^-1 (mod 26)  
        elif char.islower():
            d_text += number2char_lower( (char2number(char)*kn ) % 26 )         
        elif char == "":
            d_text += ""
        else:
            d_text += char
    return d_text





p = 'NGUYEN VIET HAO'
k = 7
c = encode(p, k)
print(c)
print(decode(c,k))