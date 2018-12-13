"""
Allan Katongole
13th December 2018
Students Mark's Grader
for Andela Level-Up
"""

def marks_grader(marks):
    above_50 = []
    below_50 = []
    print(above_50)
    print(below_50)
    for mark in marks:
        if mark > 50:
            above_50.append(mark)
        else:
            below_50.append(mark)
        if mark>=90 and mark<=100:
            print('Your mark {0} is Excellent'.format(mark))
        elif mark>=70 and mark<=89:
            print('Your mark {0} is very good'.format(mark))
        elif mark>=60 and mark<=69:
            print('Your mark {0} is good'.format(mark))
        elif mark>=40 and mark<=59:
            print('Your mark {0} is poor'.format(mark))
        elif mark>=20 and mark<=39:
            print('Your mark {0} is very poor'.format(mark))
        else:
            print('Your mark {0} is below any standard, You may need to repeat'.format(mark))

if __name__ == '__main__':
    marks_list = [23,4,5,6,64,90,67,98,45,23,67,78,89]
    print(marks_grader(marks_list))
