with open("poem.txt","r") as f:
    a= f.read()
    print(a)
    print("")
    if "twinkle" in a:
        print("the word is present")
    else:
        print("the word is not present")