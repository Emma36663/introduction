prime = True
list = []
for number in range(2,100):
    prime = True
    number += 1
    for i in range(2,number):
        if number % i == 0:
            prime = False
            break
    
    if prime:
        list.append(number)
        

print(list)

i = 1
total = 0
while i <= 100:
    total += i
    i += 1
print(total)
