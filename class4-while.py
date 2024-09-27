number = 2

while number <= 100:
    prime = True
    factor = 2
    while factor < number:
        if number % factor == 0:
            prime = False
        factor += 1
    if prime:
        print(number)
    number += 1