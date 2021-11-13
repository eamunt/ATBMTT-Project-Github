
#hoán vị các ký tự của bản rõ theo chu kỳ cố định d

def split_len(seq, length): # tách từng cụm có dộ dài length
    return [ seq[i:i + length] for i in range(0, len(seq),length) ] 

def encrypt(text, key):
    text = text.replace(" ","") #del space
    order = {
        int(val): num for num, val in enumerate(key) #[(0,'1'),(1,'2')]
    }
    e_text = ""
    for index in sorted(order.keys()):
        #sorted: sắp xếp các ký tự lại
        #print(order.keys())
        #print(index)
        for part in split_len(text, len(key)):
            print(part) #tách từng cụm 3 ký tự
            try:
                e_text += part[order[index]]# lấy vị trí order[index] trong từng phần
                print(order[index]) # index=2 => order(2)=4
                print(e_text)
            except IndexError: # hết part rồi.
                continue
    return e_text

def decrypt(e_text, key):
    e_text = e_text.replace(" ","")
    order = {
        int(val): num for num, val in enumerate(key)
    }
    d_text = ""
    n = int(len(e_text)/len(key)) # n=6/3=2
    for index in sorted(order.keys()):
        for part in split_len(e_text, n):
            try:
                d_text += part[order[index]]
            except IndexError:
                continue
    return d_text





k = "123"
c = encrypt("HAOVIE",k)
print(c)
print(list(enumerate(k)))
print(decrypt(c,k))





'''
class change_place:
    def __init__(self, mess, k):
        self.mess = mess
        self.k = k
    
    def encrypt(self):
        txt = self.mess.replace(" ", "")
        order = {
            int(val): num for num, val in enumerate(self.k)
        }
        txt_list = []
        split_ = [txt[i:i + len(self.k)] for i in range(0, len(txt), len(self.k))]
        for index in sorted(order.keys()):
            for part in split_:
                try:
                    txt_list.append(part[order[index]])
                except IndexError:
                    continue
        return "".join(txt_list)

    def decrypt(self):
        txt = self.mess.replace(" ", "")
        order = {
            int(val): num for num, val in enumerate(self.k)
        }
        txt_list = []
        n = int(len(txt) / len(self.k))
        split_ = [txt[i:i + n] for i in range(0, len(txt), n)]
        for index in sorted(order.keys()):
            for part in split_:
                try:
                    txt_list.append(part[order[index]])
                except IndexError:
                    continue
        return "".join(txt_list)


k = "12345"
mess = "hello world"

en = change_place(mess, k).encrypt()
de = change_place(en, k).decrypt()
print(en, de)
'''