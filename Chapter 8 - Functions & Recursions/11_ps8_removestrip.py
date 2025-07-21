# list=[]
# n = int(input("Enter number of sentence in the list:"))
# for i in range(n):
#     s=str(input(f"Enter {i+1} sentence:"))
#     list.append(s)
# print(list)
def remstrip(string, word):
    newstr = string.replace(word,"")
    return newstr.strip()
str = "     hello abdullah      "
n=remstrip(str,"hello")
print(n)