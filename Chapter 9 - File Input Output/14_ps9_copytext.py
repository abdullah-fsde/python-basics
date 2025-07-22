with open("this.txt") as f:
    content=f.read()
with open("thiscopy.txt","w") as f:
    content2=f.write(content)