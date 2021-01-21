import math

print("Type in function coefficients")

a = 0
b = 0
c = 0
correct_val = False

while not correct_val:
    try:
        coefficients = input().split(" ")
        a = int(coefficients[0])
        b = int(coefficients[1])
        c = int(coefficients[2])
        correct_val = True
    except:
        print("ERROR, try again")

delta = b*b - (4*a*c)
if delta >= 0:
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    print("First root: " + str(x1))
    print("Second root: " + str(x2))
else:
    print("Sorry, complex roots aren't supported")
