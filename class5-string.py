var1 = 'Hello World!'
var2 = "Runoob"
var_1 = 'Hello World!'
print("已更新字符串: ", var_1[:6] + 'Runoob!')
x = 1
print(f'{x+1=}')

print ("我叫 %s 今年 %d 岁!" % ('小明', 10))

import time

for i in range(101):
    print("\r{:3}%".format(i),end=' ')
    time.sleep(0.05)

print('\'Hello, world!\'')  

print("Hello, world!\nHow are you?") 
print("Hello, world!\tHow are you?")  

print("Hello,\b world!")  

print("Hello,\f world!") 

print("A 对应的 ASCII 值为：", ord('A'))  

print("\x41 为 A 的 ASCII 代码") 

decimal_number = 42
binary_number = bin(decimal_number)  
print('转换为二进制:', binary_number)  

octal_number = oct(decimal_number)  
print('转换为八进制:', octal_number)  

hexadecimal_number = hex(decimal_number)  
print('转换为十六进制:', hexadecimal_number) 

a = "Hello"
b = "Python"
print("a+b , jieguo:", a + b)
print("a*2 , jieguo:", a *2)
print("a[1] , jieguo:", a[1])
print("a[1:4] , jieguo:", a[1:4])

if ("H" in a ):
    print("H 在变量a中")
else:
    print("H不在结果a中")

if ("M" not in a):
    print("M is not in a ")
else:
    print("M is in a" )

print (r'\n')
print (R'\n')

