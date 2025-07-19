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
print(dict['good_guy'])
print(dict['good_guy'][0])
print(dict['dict2']['girls'][2])
dict['dict2']['girls'][2] = "huda alshammari"
print(dict['dict2']['girls'][2])