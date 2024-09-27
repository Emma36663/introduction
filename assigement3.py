num= 5
total_num = 0
for i in range(1, num+1):
    total_fac= 1
    for j in range(1, i+1):
        total_fac *= j
    total_num += total_fac

print(total_num)

n = 5
# 阶乘和
total = 0
# 代表每一个数字
for i in range(1, n + 1):
    # 当前数字的阶乘
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    total += factorial
print(total)