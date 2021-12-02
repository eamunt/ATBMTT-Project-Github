def encrypt(message, key):
    translated = ''
    charsA = LETTERS # Bảng chữ cái A-Z
    charsB = key   
    for symbol in message: # Lặp qua từng kí tự trong bản rõ
        if symbol.upper() in charsA: # Nếu là chữ cái
            symIndex = charsA.find(symbol.upper()) # Tìm index trong bảng chữ cái
            if symbol.isupper(): # In hoa?
                translated += charsB[symIndex].upper() # Thay thế kí tự
            else:
                translated += charsB[symIndex].lower()
        else:
            translated += symbol
    return translated
    
def decrypt(message, key):
    translated = ''
    charsB = LETTERS # Bảng chữ cái A-Z
    charsA = key   
    for symbol in message: # Lặp qua từng kí tự trong bản mã
        if symbol.upper() in charsA: # Nếu là chữ cái
            symIndex = charsA.find(symbol.upper()) # Tìm index trong bảng chữ cái
            if symbol.isupper(): # In hoa?
                translated += charsB[symIndex].upper() # Thay thế kí tự
            else:
                translated += charsB[symIndex].lower()
        else:
            translated += symbol
    return translated
    
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
translated = encrypt(message, key)
print('Cipher: ' + translated)
print('Plain: ' + decrypt(translated,key))