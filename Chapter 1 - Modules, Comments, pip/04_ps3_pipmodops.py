import random
print(random.randint(1, 100))
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)
colors = ["pink", "green", "blue"]
print(random.choice(colors))
#2 codes one of my own and other from the internet
from playsound import playsound
playsound('path_to_your_sound_file.mp3')