f = open('vacancy.csv',encoding="utf8").readlines()
a = []
i = 0
listoftypes = []
averageoftypes = [] #Íà êàæäûé ýëåìåíò äëÿ listoftypes áóäåò ýëåìåíò â averageoftypes ñ òåì-æå èíäåêñîì

for el in f:
    #Èíèöèàëèçàöèÿ òàáëèöû è ïîèñê òð¸õ ìàêñèìàëüíî îïëà÷èâàåìûõ âàêàíñèé
    a.append(el.split(';')[:])
    a[i][4] = a[i][4][:-1]
    if a[i][1] not in listoftypes: listoftypes.append(a[i][1]) #Çàïîëíåíèå ñïèñêà òèïîâ ðàáîò
    if i == 0:
        a[0][0] = a[0][0][1:]
        i+=1
        continue
    i+=1

for el in listoftypes:
    summa = 0
    count = 0
    for el2 in a:
        if el2[1] == el:
            count+=1
            summa +=int(el2[0])
    averageoftypes.append(summa//count)

for el in a:
    idx = 0
    for i in range(len(listoftypes)):
        print(el)
        print(listoftypes[0])
    a.append(averageoftypes[idx])
