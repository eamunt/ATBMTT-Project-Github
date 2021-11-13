def encrypt (mess):
    mess = mess.replace(" ","") #xóa khoảng trắng
    i = len(mess) - 1 # lấy ra vị trí ký tự cuối
    translated = '' #khoitao
    while i>=0:
        translated = translated + mess[i]
        i = i - 1
    return translated

def decrypt (mess_en):
    mess_en = mess_en.replace(" ","")
    i = len(mess_en) - 1
    decrypted = ''
    while i>=0:
        decrypted = decrypted + mess_en[i]
        i = i - 1
    return decrypted

mess = 'this is a program'
en = encrypt(mess)
print(en)
print(encrypt(en))

'''
class ReverseCipher:
    def __init__(self, text):
        self.text = text
        
    def encrypt(self):
        return self.text[::-1]

    def decrypt(self):
        return self.text[::-1]

message = ReverseCipher("olleH").decrypt()
print(message)
'''