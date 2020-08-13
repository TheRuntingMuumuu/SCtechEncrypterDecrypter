from runpy import run_path as r
from sys import exit
try:
    guicli = input("Would you like to use the GUI version or the CLI version? (gui/cli) ")
    guicli = guicli.lower() #make guicli lowercase so that isn't case-sensitive
    if guicli == "gui":
        r(path_name="gui.py")
    elif guicli == "cli":
        r(path_name='Encrypter.py')
    else:
        print("You did not type gui or cli")
except (KeyboardInterrupt, EOFError):
    exit("You exited the program.")
except ValueError:
    exit("FATAL: You typed an invalid entry.")
except Exception as ename:
    exit("An unknown error occured. (%s)"%ename)
