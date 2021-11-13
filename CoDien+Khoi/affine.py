def mod_inverse(x,m): # nghịch đảo của 7
    for n in range(m):
        if (x * n) % m == 1:
            return n
            break
        elif n == m - 1:
            return "Null"
        else:
            continue
class Affine(object):
    DIE = 26
    KEY = (15, 3, mod_inverse(15,26))

    def __init__(self):
        pass



    def encryptChar(self, char): # trả về chữ Hex : chr(65) = 'A'
        K1, K2, kI = self.KEY
        if char.isupper():
            return chr((K1 * (ord(char)-65) + K2) % self.DIE + 65)
        elif char.islower():
            return chr((K1 * (ord(char)-97) + K2) % self.DIE + 97)
        else:
            return char
        # ax + b mod 26

    def encrypt(self, string):
        return "".join(map(self.encryptChar, string)) # map() duyệt tất cả cấc phần tử của 1 iterable(list,dict...) qua 1 hàm cho trước và trả về kết quả 1 list kết quả sau khi thực thi.
        # join(): các phần tử lại khi thực thi xong map()

    def decryptChar(self, char):
        K1, K2, KI = self.KEY
        if char.isupper():
            return chr(KI * ((ord(char)-65) - K2) % self.DIE + 65)
        elif char.islower():
            return chr(KI * ((ord(char)-97) - K2) % self.DIE + 97)
        else:
            return char   
        # a^-1 *(y-b) mod 26

    def decrypt(self, string):
        return "".join(map(self.decryptChar, string))

    
affine = Affine()
p = 'On August I Will Go'
c = affine.encrypt(p)
print (affine.KEY)
print (c)
print(affine.decrypt(c))