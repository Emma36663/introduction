def calculate_time(a,b,c,d):
    second = 0
    if c >= a:
        second += 60*(c-a)
    else:
        second += 60*(24+c-a)
    second += (d-b)
    print(second)
    

calculate_time(9,10,10,50)
calculate_time(9,50,10,20)
calculate_time(23,50,2,30)