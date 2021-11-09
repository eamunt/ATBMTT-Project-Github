
def encrypt(text, n):
    a = []
    e_text = ''
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()): 
            e_text += chr( (ord(char) - 65 + n)%26 +65) 
        elif (char.islower()):
            e_text += chr( (ord(char) - 97 + n)%26 +97)
        else:
            e_text += e_text
    return e_text


def decrypt(e_text, n):
    a = []
    d_text = ''
    for i in range(len(e_text)):
        char = e_text[i]
        if (char.isupper()): 
            d_text += chr( (ord(char) - 65 - n)%26 +65) 
        elif (char.islower()):
            d_text += chr( (ord(char) - 97 - n)%26 +97)
        else:
            d_text += d_text
    return d_text



p = 'thursday'
n=13
c = encrypt(p, n)
print(c)
print(decrypt(c, n))