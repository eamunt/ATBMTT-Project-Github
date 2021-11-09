


'''
class single_replace_cipher:
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def __init__(self, mess, k):
        # self.
        self.k = k
        self.mess = mess

    def encrypt(self):
        encr = []
        for symbol in self.mess:
            if symbol.upper() in self.LETTERS:
                sym_index = self.LETTERS.find(symbol.upper())
                if symbol.isupper():
                    encr.append(self.k[sym_index].upper())
                else:
                    encr.append(self.k[sym_index].lower())
            else:
                encr.append(symbol)
        return "".join(encr)

    def decrypt(self):
        encr = []
        for symbol in self.mess:
            if symbol.upper() in self.k:
                sym_index = self.k.find(symbol.upper())
                if symbol.isupper():
                    encr.append(self.LETTERS[sym_index].upper())
                else:
                    encr.append(self.LETTERS[sym_index].lower())
            else:
                encr.append(symbol)
        return "".join(encr)

en = single_replace_cipher('defend the east wall of the castle', 'PHQGIUMEAYLNOFDXJKRCVSTZWB').encrypt()
de = single_replace_cipher(en, 'PHQGIUMEAYLNOFDXJKRCVSTZWB').decrypt()
print(en, de)
'''