def encodeVer1(text, encryptionKey=8): #for Encryption
    """
    This is one of the ways that the text can be encrypted. It is very simple.
    parameter text: Decrypted (original) text
    parameter encryptionKey: Encryption key (should be integer of length 1, of value 1, 2, 3, 4, 5, 6, 7, or 8). For backwards compatibility purposes, defaults to 8.
    You could do more than 8 but it's untested and not very useful.
    """
    encodedText = list(text)
    length = len(encodedText)
    for i in range(0,length):
        encodedText[i] = ord(encodedText[i])
    for i in range(0,length):
        if encodedText[i] != 32:
            encodedText[i] = encodedText[i] - int(str(encryptionKey)[0])
    for i in range(0,length):
        encodedText[i] = str(chr(encodedText[i]))
    encodedText = ''.join(encodedText)
    return encodedText
def decryptVer1(text, encryptionKey=8): #for Decryption
    """
    This is one of the ways text can be decrypted.
    parameter text: Encrypted text
    parameter encryptionKey: The encryption key (should be integer of length 1, of value 1, 2, 3, 4, 5, 6, 7, or 8). For backwards compatibility purposes, defaults to 8.
    You could do more than 8 but it's untested and not very useful.
    """
    decodedText = list(text)
    length = len(decodedText)
    for i in range(0,length):
        decodedText[i] = ord(decodedText[i])
        if decodedText[i] != 32:
            decodedText[i] = decodedText[i] + int(str(encryptionKey)[0])
        decodedText[i] = str(chr(decodedText[i]))
    decodedText = ''.join(decodedText)
    return decodedText
