from tkinter import * #import the submodules of tkinter
from tkinter import messagebox #import messagebox
from sys import exit #import the exiting function
main = Tk()
yn = messagebox.askyesno("Agree?", "With these terms: do not distribute without permission.")
if yn is True:
    messagebox.showinfo("You agreed", "You can now use the Software")
else:
    messagebox.showerror("Error!", "You did not agree!")

main.mainloop()
