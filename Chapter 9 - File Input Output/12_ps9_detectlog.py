with open("log.txt","r") as f:
    content = f.read()
if "python" in content.lower():
    print("Yes it is present")
else:
    print("No it is not present")