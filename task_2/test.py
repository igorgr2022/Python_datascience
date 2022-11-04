import numpy as np
from numpy.random import randint

#todo Создать с помощью электронной таблицы матрицу с какими-либо данными
# x = np.random.randint(1,100, (15,15))    #! создаю матрицу 15 на 15
# np.savetxt('x.txt', x)                   #! сохраняю матрицу в файл
#! открываю чистый  excel
#! лист ==>  вставить лист из файла
#! сохраняю файл Matrix.csv

#todo Загрузите данные из электронной таблицы в матрицу numpy.
z1 = np.genfromtxt('/home/workivan/Python-datascience/Matrix.csv', delimiter='^')
print('z1:')
print(z1)

#todo Создайте единичную матрицу размерности, идентичной полученной из электронной таблицы.
z2 =np.eye(15)
print('z2:')
print(z2)

#todo Перемножьте одно на другое и экспортируйте результат в электронную таблицу.
z3 = np.zeros((15, 15))
print('z3:')
print(z3)
for i in range(15):
    for b in range(15):
        z3[i][b] = z1[i][b] * z2[i][b] 

print('z3:')
print(z3)
np.savetxt('z3.txt', z3)  #! сохраняю полученную матрицу z3 в файл z3.txt
#! экспортирую результат из z3.txt в таблицу file_export_z3.csv
