s = '123'
s1 = '456'
#拼接字符串
s += s1
s = s.lstrip("12")
s = s.rstrip("6")
# 去除首尾
s = s.strip("5") 
#格式化字符串
s += ('{},testformat,{}').format("l","j")
for char in s:
    print(char)