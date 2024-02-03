f = open('vacancy.csv',encoding="utf8").readlines()
a = []
i = 0
maxarray = [0,0,0]

for el in f:
    #Инициализация таблицы и поиск трёх максимально оплачиваемых вакансий
    a.append(el.split(';')[:])
    a[i][4] = a[i][4][:-1]
    if i == 0:
        a[0][0] = a[0][0][1:]
        maxarray[0] = a[0]
        maxarray[1] = a[0]
        maxarray[2] = a[0]
        i+=1
        continue
    salary = int(a[i][0])
    if salary > int(maxarray[0][0]):
        maxarray[0] = a[i]
    elif salary > int(maxarray[1][0]):
        maxarray[1] = a[i]
    elif salary > int(maxarray[2][0]):
        maxarray[2] = a[i]
    i+=1
print("Top 3 best jobs available salary-wise:")
for el in maxarray:
    print('Company: ', el[4], '; Salary: ', el[0], '; Work type: ', el[1], '; Role: ', el[3], '; Company size: ', el[2],sep = '')
