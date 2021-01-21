print("Enter new key please")
org_key = str(input())

correct_key = False
while correct_key is False:
    print("Enter key:")
    key = str(input())

    if key != org_key:
        print("Key is incorrect!")
    if key == org_key:
        print("Correct key!")
        correct_key = True
