import re

# # 1 task
# pas = input('Введите пароль: ')    #my-p@sswOrd
# reg = '[0-9A-Za-z@_-]{6,18}'
# print('Ваш пароль надёжный: ',re.findall(reg,pas))

# # 2 task
test = 'В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков.'
reg = r'[0-3][0-9]/[0-1][0-9]/[1-2][0-9][0-9][0-9]'
print(re.findall(reg, test))