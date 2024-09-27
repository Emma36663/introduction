import operator
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1,2,3,4,5]
list3 = ["a","b","c","d"]
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']

print(list4[0])
print(list4[1])
print(list4[2])

print(list4[-1])
print(list4[-2])
print(list4[-3])

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(nums[0:4])

list5 = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]
print ("list5[1]: ", list5[1])
print ("list5[1:-2]: ", list5[1:-2])

list1.append('Baidu')
print(list1)


list = ['Google', 'Runoob', 1997, 2000]
print(list)
del list[2]
print(list)

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])

a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a,b))
print("operator.eq(c,b): ", operator.eq(c,b))
