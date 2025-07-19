dict = {}
name1 = input("Enter your name: ")
fav_lang1 = input("Enter your favorite language: ")
name2 = input("Enter your friend's name: ")
fav_lang2 = input("Enter your friend's favorite language: ")
name3 = input("Enter your second friend's name: ")
fav_lang3 = input("Enter your second friend's favorite language: ")
name4 = input("Enter your third friend's name: ")  
fav_lang4 = input("Enter your third friend's favorite language: ")
dict = {
    name1: fav_lang1,
    name2: fav_lang2,
    name3: fav_lang3,
    name4: fav_lang4
    }
print(dict)
# if names are not unque the name with latest update will be added in the dictionary
# if languages are same then it will be returned as it is