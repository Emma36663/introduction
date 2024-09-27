number_fish = 6
fish = [-4,-3,0,-5,-1,-2]
max = fish[0]
min = fish[0]

for i in range(number_fish): # choose the current fish
    if fish[i] < min:
        min = fish[i]
    elif fish[i] > max:
         max = fish[i]

print(min)
print(max)
