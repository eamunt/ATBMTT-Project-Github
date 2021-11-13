import base64



def encrypt(text):
    text_bytes = text.encode('ascii')
    base64_bytes = base64.b64encode(text_bytes)
    base64_text = base64_bytes.decode('ascii')

    return base64_text

def decrypt(en_text):
    base64_bytes = en_text.encode('ascii')
    entext_bytes = base64.b64decode(base64_bytes)
    de_text = entext_bytes.decode('ascii')

    return de_text

p = "rav"
c = encrypt(p)
print(c)
print(decrypt(c))