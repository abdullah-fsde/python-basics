# with open("log.txt","r") as f:
#     content = f.read()
# if "python" in content.lower():
#     print("Yes it is present")
# else:
#     print("No it is not present")
with open("log.txt", "r") as f:
    lines = f.readlines()

word = "python"
for i, line in enumerate(lines, start=1):
    if word in line:
        print(f"Found on line {i}")