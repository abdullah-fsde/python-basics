dict = {
    "acha" : "good",
    "Bura" : "bad",
    "bekaar" : "useless",
    "kamzor" : "weak",
    "mazboot" : "strong",
    "dost" : "friend"
}
print(dict.keys())
x = input("Enter a word in Hinglish: ")
print("The meaning of ",x ,"is: ",dict.get(x))