import os

files = ["./test/1.jpg", "./test/2.jpg", "./test/3.jpg", "./test/4.jpg"]
new_extension = ".png"

for file in files:
    pre, ext = os.path.splitext(file)
    os.rename(file, pre + new_extension)
