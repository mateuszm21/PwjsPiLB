import json

if __name__ == '__main__':
    run = True

    while run:
        print("Choose operation: [S]how data, [A]dd data, [D]elete entrance, [G]enerate file, [E]xit")
        menu = input()
        try:
            if menu == "E":
                run = False

            elif menu == "S":
                with open('data.txt') as json_file:
                    data = json.load(json_file)
                    for p in data['Books']:
                        print('name: ' + p['name'])
                        print('genre: ' + p['genre'])
                        print('author: ' + p['author'])
                        print('')

            elif menu == "G":
                data = {}
                data['Books'] = []
                data['Books'].append({
                    'name': 'Da Vinci Code',
                    'genre': 'Thriller',
                    'author': 'Brown, Dan'
                })
                data['Books'].append({
                    'name': 'Harry Potter and the Deathly Hallows',
                    'genre': 'Fiction',
                    'author': 'Rowling, J.K.'
                })
                data['Books'].append({
                    'name': 'New Moon',
                    'genre': 'Fiction',
                    'author': 'Meyer, Stephenie'
                })

                with open('data.txt', 'w') as outfile:
                    json.dump(data, outfile)

            elif menu == "A":
                print("Enter book's: name, genre and author")
                menu = input()
                try:
                    chunks = menu.split()
                    with open('data.txt') as json_file:
                        data = json.load(json_file)
                        data['Books'].append({
                            'name': chunks[0],
                            'genre': chunks[1],
                            'author': chunks[2]
                        })
                        with open('data.txt', 'w') as outfile:
                            json.dump(data, outfile)
                except:
                    print("Error")

            elif menu == "D":
                print("Enter entrance number to be deleted:")
                menu = input()
                try:
                    with open('data.txt') as json_file:
                        data = json.load(json_file)
                        del data["Books"][int(menu)]
                    with open('data.txt', 'w') as outfile:
                        json.dump(data, outfile)
                except:
                    print("Error")
        except:
            print("Error")
