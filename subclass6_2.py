number_fish = 6
fish = [4,3,0,5,1,2]
max = 0
min = 0
for i in range(number_fish): # choose the current fish
    num = 0
    for j in range(i):
        if fish[i] > fish[j]:
            num += 1
    print(num)

for i in range(number_fish): # choose the current fish
    num = fish[i]
    if num < min:
        min = num
    elif num > max:
         max = num

print(min)
print(max)

