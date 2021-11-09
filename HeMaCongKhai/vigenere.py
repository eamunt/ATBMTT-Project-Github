def encrypt(plaintext, key):
    key = key.replace(" ","")
    key_length = len(key) #
    plaintext = plaintext.replace(" ","")
    key_as_int = [ord(i) for i in key] # 
    plaintext_int = [ord(i) for i in plaintext] #same
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value+ord('A'))
    return ciphertext
def decrypt(ciphertext, key):
    key = key.replace(" ","")
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext = ciphertext.replace(" ","")
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value+ord('A'))
    return plaintext
p = "HOMNAYLATHUSAU"
k = "CIP"
c = encrypt(p,k)
print (c)
print(p)
print (decrypt(c,k))
