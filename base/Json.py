import json

data = {"name": "John", "age": 30, "city": "New York"}

#将json转为字符串
json_string = json.dumps(data)

print(json_string)

#将字符串转为Json
json_Object = json.loads(json_string)
print(json_Object)



