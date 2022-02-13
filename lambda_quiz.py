import openpyxl
import random

wb = openpyxl.load_workbook('lambda_quiz.xlsx')
ws = wb['Sheet1']

max_num = ws.max_row
print(max_num)
print('start? :')
quiz = input('quit : Enter')

while quiz:
    rand_num = random.randint(2, max_num + 1)
    print()
    print(ws['B' + str(rand_num)].value)
    print()
    input()
    print(ws['C' + str(rand_num)].value)
    print('continue? enter any key except not enter key only')
    quiz = input()
