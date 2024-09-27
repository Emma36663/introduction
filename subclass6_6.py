num = 20
list = [20]
while num != 1:
    if num % 2 == 1:
        num = num*3 + 1
        list.append(int(num))
    else:
        num = num/2
        list.append(int(num))
list.reverse()
print(list)