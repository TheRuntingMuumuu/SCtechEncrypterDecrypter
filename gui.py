from tkinter import * #import the submodules of tkinter
from tkinter import messagebox #import messagebox
from sys import exit #import the exiting function
number = 0
main = Tk()
main.title("SCtech encryptor")
yn = messagebox.askyesno("Agree?", "With these terms: do not distribute without permission.")
if yn is True:
    messagebox.showinfo("You agreed", "You can now use the Software")
else:
    messagebox.showerror("Error!", "You did not agree!")
    exit()

textBox = Entry(main)
textBox.pack()
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
    toEncrypt = textBox.get()
    encryptedText = encodeVer1(toEncrypt)
    global number
    number = number + 1
    textTitle = "Result #", number
    messagebox.showinfo("The result", encryptedText)
    window1 = Toplevel() #Source: daniweb.com/programming/software-development/code/442746/toplevel-child-window-example-tkinter-python
    window1.title(textTitle)
    textt = "Result number ", number, ":"
    Label(window1, text=textt).pack()
    w = Text(window1, height=1, borderwidth=0) #SOURCE: stackoverflow.com/questions/1602106/in-pythons-tkinter-how-can-i-make-a-label-such-that-you-can-select-the-text-wi
    w.insert(1.0, encryptedText)
    w.pack()
    w.configure(state="disabled")
def decrypt():
    toDecrypt = textBox.get()
    decryptedText = decryptVer1(toDecrypt)
    global number
    number = number + 1
    window1 = Toplevel() #Source: daniweb.com/programming/software-development/code/442746/toplevel-child-window-example-tkinter-python
    window1.title('Result #', number)
    textt = "Result number ", number, ":"
    Label(window1, text=textt).pack()
    messagebox.showinfo("The result", decryptedText)
    w = Text(main, height=1, borderwidth=0)
    w.insert(1.0, decryptedText)
    w.pack()
    w.configure(state="disabled")

Button(main, text="Encrypt Text", command=encrypt).pack()
Button(main, text="Decrypt Text", command=decrypt).pack()

main.mainloop()
