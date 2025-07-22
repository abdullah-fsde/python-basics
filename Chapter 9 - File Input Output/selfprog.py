
def game(char):
    score=0
    if char=="King":
        score="100"
    elif char=="Queen":
        score="75"
    elif char=="Slave":
        score="50"
    elif char=="Police":
        score="25"
    elif char=="Thief":
        score="0"

    print(score)
    with open("hi-score.txt","w") as f:
        f.write(score)
print("1.King")
print("2.Queen")
print("3.Slave")
print("4.Police")
print("5.Thief")
char = int(input("Enter Your Choice :"))
if char == 1:
    char="King"
elif char == 2:
    char="Queen"
elif char == 3:
    char="Slave"
elif char == 4:
    char="Police"
elif char == 5:
    char="Thief"
else:
    print("enter valid choice")

game(char)
