list1=["there","we","abdullah","donkey"]
with open("listreplace.txt") as f:
    content = f.read()
for i in range(len(list1)):
    if list1[i] in content:
        content = content.replace(list1[i],"$@#%^$")

with open("listreplace.txt","w") as f:
    f.write(content)