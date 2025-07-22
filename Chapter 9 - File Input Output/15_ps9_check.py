with open("this.txt") as f:
    content=f.read()
with open("thiscopy.txt") as f:
    content2=f.read()
if content == content2:
    print("Both are identical")
else:
    print("Both are not same")