import os

for root, dirs, files in os.walk(".", topdown=False):
    print(root)
    print(dirs)
    print(files)

