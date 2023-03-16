l = {"name":10,"number":2}
print(l.get("name"))
# l.clear()
# print(l)

#lambad排序字典
l1 = sorted(l.items(), key=lambda x: x[1])
print(l1)