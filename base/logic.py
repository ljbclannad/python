x = 3
y = 2
if x < y :
    print("x<y")
elif x >y :
    print("x>y")

d = {'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'}
for k in d: # 遍历字典的键
    print(k)

for v in d.values(): # 遍历字典的值
    print(v)

for k, v in d.items(): # 遍历字典的键值对
    print('key: {}, value: {}'.format(k, v))

l = [1, 2, 3, 4, 5, 6, 7]
for index in range(0,len(l)):
    if index < 5:
        print(l[index])
for index,item in enumerate(l):
    if index <5:
        print(item)




