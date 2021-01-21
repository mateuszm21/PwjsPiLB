files_list = ["Volt.txt", "Witchcraft.txt", "Zinc.txt"]
word_dict = {" and ": " as well as ",
             " is ": " ERROR ",
             " of ": " because of "}

for file in files_list:
    new_string = []
    with open(file, 'r') as data:
        for line in data:
            for word in word_dict:
                if word in line:
                    line = line.replace(word, word_dict[word])
            new_string.append(line)

    with open(file, 'w') as data:
        for line in new_string:
            data.write(line)
