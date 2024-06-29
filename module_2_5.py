# Напишите функцию get_matrix с тремя параметрами n, m и value,
# которая будет создавать матрицу(вложенный список) размерами n
# строк и m столбцов, заполненную значениями value и возвращать
# эту матрицу в качестве результата работы.

def showMatrix(matrix):
    typeTemplate = []
    if type(matrix) != type(typeTemplate):
        print('Неверный тип аргумента!')
        return
    else:
        for i in matrix:
            for j in range(len(i)):
                print(i[j], end = ' ')
            print('')
def returnList(count, value):
    tempList = []
    for i in range(count):
        tempList.append(value)
    return tempList

def getMatrix(n = 2, m = 2, value = 3):
    matrixList = []
    for i in range(n):
        matrixList.append(returnList(m, value))
    return matrixList
#-----------------------------------------------

matrix = getMatrix(3, 3, 9)
print(matrix)
showMatrix(matrix)

showMatrix(5)

matrix = getMatrix()
showMatrix(matrix)

listParam = [4, 4, 6]
matrix = getMatrix(*listParam)
showMatrix(matrix)
