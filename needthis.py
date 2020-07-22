def encodeVer1(text): #for Encryption
    """
    This is one of the ways that the text can be encrypted. It is very simple.
    Syntax: encodeVer1(text)
    """
    encodedText = list(text)
    length = len(encodedText)
    for i in range(0,length):
        encodedText[i] = ord(encodedText[i])
    for i in range(0,length):
        if encodedText[i] != 32:
            encodedText[i] = encodedText[i] - 8
    for i in range(0,length):
        encodedText[i] = str(chr(encodedText[i]))
    encodedText = ''.join(encodedText)
    return encodedText
def decryptVer1(text): #for Decryption
    """
    This is one of the ways text can be decrypted.
    Syntax: decryptVer1(encrypted_text)
    """
    decodedText = list(text)
    length = len(decodedText)
    for i in range(0,length):
        decodedText[i] = ord(decodedText[i])
        if decodedText[i] != 32:
            decodedText[i] = decodedText[i] + 8
        decodedText[i] = str(chr(decodedText[i]))
    decodedText = ''.join(decodedText)
    return decodedText
