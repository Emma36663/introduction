target = -10
number_fish = 6
fish = [-4,-3,0,-5,-7,-2]
j = False
k = False

for i in range(number_fish):
    if target == fish[i]:
        j = True

if j:
    print('Yes')
else:
    print('No')

for a in range(number_fish):
    for b in range(number_fish):
        if a + b == target:
            k = True
            if a == b:
                k = False
if k:
    print('Yes')
else:
    print('No')

print(k)