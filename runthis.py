from runpy import run_path as r
from sys import exit
try:
    r(path_name='Encrypter.py')
except (KeyboardInterrupt, EOFError):
    exit("You exited the program.")
except:
    exit("An unknown error occured.")
