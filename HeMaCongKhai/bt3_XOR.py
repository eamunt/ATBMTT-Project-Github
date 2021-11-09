def dec2bin(num):
    res = bin(num).replace("0b", "")
    if(len(res)%4 != 0):
        div = len(res) / 4
        div = int(div)
        counter =(4 * (div + 1)) - len(res)
        for i in range(0, counter):
            res = '0' + res
    return res


def bin2hex(s):
    mp = {"0000" : '0',
        "0001" : '1',
        "0010" : '2',
        "0011" : '3',
        "0100" : '4',
        "0101" : '5',
        "0110" : '6',
        "0111" : '7',
        "1000" : '8',
        "1001" : '9',
        "1010" : 'A',
        "1011" : 'B',
        "1100" : 'C',
        "1101" : 'D',
        "1110" : 'E',
        "1111" : 'F' }
    hex = ""
    for i in range(0,len(s),4):
        ch = ""
        ch = ch + s[i]
        ch = ch + s[i + 1]
        ch = ch + s[i + 2]
        ch = ch + s[i + 3]
        hex = hex + mp[ch]
    return hex


def encrypt(text, k):
    bi_text = ''
    en_text = ''
    for i in range(len(text)):
        char = text[i]
        bi_text += dec2bin(ord(char)) # get char text to bin

    bi_key = ''
    for j in range(len(k)):
        char_k = k[j]
        bi_key += dec2bin(ord(char_k)) # get char key to bin

    
    for h in range(len(bi_text)):
        x1 = int(bi_text[h]) # get 1 bit to int
        if h < len(bi_key): 
            x2 =int(bi_key[h])
        else: 
            x2 = int(bi_key[h%len(bi_key)]) # if len bi_text > then get mod len bi_key
        xo_r = x1^x2 # xor
        en_text += str(xo_r) # return
    
    hhh = bin2hex(en_text)
    return hhh

    #xor
        
        




p = 'GOOD'
k='ABC'
c = encrypt(p,k)
print(c)
#print(decrypt(c))