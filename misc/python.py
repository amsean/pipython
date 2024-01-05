
# while(1):
#     x = int(input('Input Your First Number: '))
#     z = x % 2
#     if x > 0 and z == 0:
#         print('Positive and Even')
#     if x > 0 and z != 0:
#         print('Positive and Odd')
#     
#     if x==0:
#         print('Zero')

# x = 1
# while x <= 10:
#     print(x)
#     x = x + 1
# print('Thats all folks!')

# import numpy as np
# for i in np.linspace(1, 10, 19):
#     print(i)

numGrades = int(input('How Many Grades? '))
x = []
for i in range(0, numGrades, 1):
    myGrade = int(input('Input Your Grade: '))
    x.append(myGrade)
print('Your Grades Are: ')
for i in range(0, numGrades, 1):
    print(x[i])







