# filehandler
# context manager
# with - context manager w pythonie

# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open("test.log", "w", encoding='utf-8') as f:
    f.write("Powitanie\n")

# f.write("l") # ValueError: I/O operation on closed file.

# x - gdy plik istnieje mamy odpowiedni komunikat
# FileExistsError: [Errno 17] File exists: 'test.log'
# with open("test.log", "x") as f:
#     f.write("Powitanie\n")

with open("test.log", "w",  encoding='utf-8') as f:
    f.write("Powitanie2\n")

# a - dodanie do istniejącego pliku
with open("test.log", "a",  encoding='utf-8') as f:
    f.write("Dodane\n")
    f.write("Dodane2\n")
    f.write("Dodane23\n")
    f.write("Dodśćźane23\n")

# r - odczyt
with open("test.log", "r",  encoding='utf-8') as f:
    lines = f.read()

print(lines)
# Powitanie2
# Dodane
# Dodane2
# Dodane23