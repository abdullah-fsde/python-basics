name = input("Enter your name: ")
date = input("Enter today's date: ")
letter = '''Dear {name},
you are selected!
{date}'''
print(letter.format(name=name, date=date))
