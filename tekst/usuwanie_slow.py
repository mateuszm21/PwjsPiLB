files_list = ["Volt.txt", "Witchcraft.txt", "Zinc.txt"]
word_list = [" and ", " is ", " of "]

for file in files_list:
    new_string = []
    with open(file, 'r') as data:
        for line in data:
            for word in word_list:
                if word in line:
                    line = line.replace(word, " ")
            new_string.append(line)

    with open(file, 'w') as data:
        for line in new_string:
            data.write(line)
