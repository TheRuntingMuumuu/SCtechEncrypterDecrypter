from tkinter import * #import the submodules of tkinter
from tkinter import messagebox #import messagebox
from sys import exit #import the exiting function
main = Tk()
yn = messagebox.askyesno("Agree?", "With these terms: do not distribute without permission.")
if yn is True:
    messagebox.showinfo("You agreed", "You can now use the Software")
else:
    messagebox.showerror("Error!", "You did not agree!")
    exit()

entry = Entry(root)
def encodeVer1(text):
    """This is one of the ways that the text can be encrypted. It is very simple."""
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
def decryptVer1(text):
    """this is one of the ways that text can be decrypted."""
    decodedText = list(text)
    length = len(decodedText)
    for i in range(0,length):
        decodedText[i] = ord(decodedText[i])
        if decodedText[i] != 32:
            decodedText[i] = decodedText[i] + 8
        decodedText[i] = str(chr(decodedText[i]))
    decodedText = ''.join(decodedText)
    return decodedText
def encrypt():
    #Until there are multiple versions I will not be asking for which version.
    toEncrypt = entry.get()
    encryptedText = encodeVer1(toEncrypt)
    messagebox.showinfo("The result", encryptedText)
def decrypt():
    toEncrypt = entry.get()
    decryp

main.mainloop()
