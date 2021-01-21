import random
import copy

random_list = []
new_list = []
new_list2 = []

for i in range(0, 49):
    n = random.randint(1, 30)
    random_list.append(n)

print(random_list)

new_list2 = copy.deepcopy(random_list)
new_list2.sort()
new_list2.reverse()

while random_list:
    minimum = random_list[0]
    for x in random_list:
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    random_list.remove(minimum)

new_list.reverse()

print(new_list)
print(new_list2)
