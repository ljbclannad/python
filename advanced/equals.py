import copy
a = 10
b = 10

print(a==b)
print(id(a))
print(id(b))
print(a is b)

t1 = (1,2,[3,4])
print(t1[-1].append(5))


#x是一个无限嵌套的列表，y深度拷贝x也是一个无限嵌套的列表，理论上x==y应该返回True，但是x==y内部执行是会递归遍历列表x和y中每一个元素的值，由于x和y是无限嵌套的，因此会stack overflow
x = [1]
x.append(x)

y = copy.deepcopy(x)
# print(x==y)

l1 = [1,2,3]
l2 = [1,2,3]
l3 = l2

print(l1 is l2)
print(l1 is l3)
print(l2 is l3)