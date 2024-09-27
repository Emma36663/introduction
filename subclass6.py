numbers = [4,2,1,9,10]
n = len(numbers)
for i in range(0,n):
    print(numbers[i])
sum = 0
for i in range(0,n):
    sum += numbers[i]
print(sum)

print('\n')
for i in range(0,n):
    prime = True
    number = numbers[i] 
    factor = 2
    while factor < number:
        if number % factor == 0:
            prime = False
        factor += 1
    if prime:
        print(number)