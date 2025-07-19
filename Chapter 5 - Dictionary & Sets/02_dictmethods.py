dict = {
    'abdullah' : 'good guy',
    'abdul' : 'bad guy',
    'abdulaziz' : 'good guy',
    "good_guy" : [2, 0],
    'bad_guy' : [0, 1],
    "dict2" : {
        "girls" : ["sara", "nora", "huda"],
        "abdullah" : 'professor',
        "abdul" : 'student'
    }
}
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get('dict2'))
updateddict = {
    "boys" : ["suresh ", "ramesh", "mahesh"],
    "abdullah" : 'teacher',
    "abdul" : 'learner'
}
dict.update(updateddict)
print(dict)