def mod_inverse(x,m): #tìm nghịch đảo của 7 sẽ là 15
    for n in range(m):
        if (x * n) % m == 1:
            return n
            break
        elif n == m - 1: #không tìm được nghịch đảo
            return "Null"
        else:
            continue
KEY = (7, 3, mod_inverse(7,26) )        
def encryptChar(char):
    K1, K2, kI = KEY
    if (char.isupper()):
        return chr((K1 * (ord(char)-65) + K2) % 26 + 65)
    elif char.islower():
        return chr((K1 * (ord(char)-97) + K2) % 26 + 97)
    elif char == ' ':
        return ''
    else:
        return char

def encrypt(string):
    str = ''
    for char in string:
        str += encryptChar(char)
    return str
    
def decryptChar(char):
    K1, K2, KI = KEY
    if (char.isupper()):
        return chr(KI * ((ord(char)-65) - K2) % 26 + 65)
    elif char.islower():
        return chr(KI * ((ord(char)-97) - K2) % 26 + 97)
    else:
        return char
    
def decrypt(string):
    str = ''
    for char in string:
        str += decryptChar(char)
    return str    
    
p = 'Infor@mation Sec'
c = encrypt(p)
print (KEY)
print (c)
print(decrypt(c))