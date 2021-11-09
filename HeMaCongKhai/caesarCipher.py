#N=26
def encrypt(text, k):
    text = text.replace(" ","") #del space
    e_text = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()): #isupper
            e_text += chr((ord(char) + k - 65) % 26 + 65) 
        else: #islower
            e_text += chr((ord(char) + k - 97) % 26 + 97) 
    return e_text

def decrypt(e_text, k):
    e_text = e_text.replace(" ","")
    d_text = ""
    for i in range(len(e_text)):
        char = e_text[i]
        if char.isupper():
            d_text += chr((ord(char) -k - 65) % 26 + 65)
        else:
            d_text += chr((ord(char) +k - 97) % 26 + 97)
    return d_text



k = 4
text = "THIS IS A PROGRAM"
e = encrypt(text,k)
print(e)
print(decrypt(e,k))


'''
def transition_code(message, key):
    lower_unicode = 97
    upper_unicode = 65
    alphabet_length = 26
    result = ''

    for char in message:
        # new_char = (char + k) mod 26
        if char.isupper():
            # char => unicode => char
            result += chr(((ord(char) - upper_unicode + key) % alphabet_length) + upper_unicode)
        elif char.islower():
            result += chr(((ord(char) - lower_unicode + key) % alphabet_length) + lower_unicode)
        else:
            # special char
            result += char

    return result


def encode(message, key):
    return transition_code(message, key)


def decode(message, key):
    return transition_code(message, -key)


plaintext = 'you'
k = 3
print('Key is: ', k)
c = encode(plaintext, k)
print("Cipher text: ", c)
print("Plain text: ", decode(c, k))
'''

