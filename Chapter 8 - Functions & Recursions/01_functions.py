def percent(marks):
    p = ((marks[0] + marks[1] + marks[2] + marks[3])/4)*100 #or could be written as (sum(marks)/4)*100
    return p
marks1 = [25,45,85,65]
percent1= percent(marks1)
marks2=[52,54,58,56]
percent2=percent(marks2)
print(f'''the percentage of {marks1} is {percent1}
the percentage of {marks2} is {percent2}''')