import re

with open("/Users/lejinbo/Downloads/drug.sql","r") as f:
    contents = f.read()
    print(contents)

with open("/Users/lejinbo/Downloads/testPythonInput.txt","w") as f:
    f.write(contents)
