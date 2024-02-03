f = open('vacancy.csv',encoding="utf8").readlines()
a = []
i = 0
for el in f:
    #Инициализация таблицы
    a.append(el.split(';')[:])
    a[i][4] = a[i][4][:-1]
    i+=1

while True:
    #Процесс программы
    lista = []
    print('Input company name')
    b = input()
    if b == 'None':
        #Сценарий остановки программы
        break

    for j in range(len(a)):
        #Поиск нужной компании в списке
        if a[j][4] == b: 
            lista.append(a[j])
    if len(lista):
        #Вывод вакансий
        for el in lista:
            print('Salary: ', el[0], '; Work type: ', el[1], '; Role: ', el[3], '; Company size: ', el[2],sep = '')
    else:print('Unfortunately, nothing was found')