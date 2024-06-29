def get_matrix(n, m, value):               #объявил функцию get_matrix и записал внутри неё параметры n, m, value
    matrix = []                            #создал пустой список matrix внутри функции get_matrix
    for i in range(n):                     #создал внешний цикл for для количества строк n
        string = []                        #внутри внешнего цикла for создал пустой список
        for j in range(m):                 #создал внутренний цикл for для количества столбцов m
            string.append(value)           #в пустой список string добавил значение value
        matrix.append(string)              #внутри функции get_matrix вернул matrix со списком string
    return matrix                          #запустил matrix

result1 = get_matrix(2, 2, 10) #n - это количество строк, m - количество столбцов, value - значение, result - разные результаты с разными значениями
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)