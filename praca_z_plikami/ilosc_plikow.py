import os

directory = "."
print(len(next(os.walk(directory))[2]))
