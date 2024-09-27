numbers = [1,1,3,2,1,5,3,2]
list = []
for i in range(len(numbers)):
    for j in range(len(numbers)):
        num = 0
        if numbers[i] == numbers[j]:
            num += 1
    print(numbers[i])
    print(" ".join(str(num)))