target = -10
number_fish = 6
fish = [-4,-3,0,-5,-7,-2]
k = False

for a in range(number_fish):
    for b in range(a+1, number_fish):
        if fish[a] + fish[b]== target:
            k = True

if k:
    print('Yes')
else:
    print('No')

print(k)