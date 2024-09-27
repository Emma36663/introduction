print("要游多远？")
total_distance = float(input())
one_step = 2
total_step = 0
present_distance = 0
while present_distance < total_distance:
    present_distance += one_step
    total_step += 1
    print(one_step, "one step")
    print(total_step, "total step")
    print(present_distance, "present distance")
    one_step = one_step*0.98
print(total_step)