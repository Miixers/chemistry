kat_1 = input(": ")
kat_2 = input(": ")
an_1 = input(": ")
an_2 = input(": ")
soed_1 = kat_1 + an_1
soed_2 = kat_1 + an_2
soed_3 = kat_2 + an_1
soed_4 = kat_2 + an_2
reags = [soed_1, soed_2, soed_3, soed_4]
results = []
osadok = 0
if reags[3] == "hoh" or reags[3] == osadok:
         del reags[3]
         results.append(soed_4)
         kicked = 4
if reags[2] == "hoh" or reags[2] == osadok:
         del reags[2]
         results.append(soed_3)
         kicked = 3
if reags[1] == "hoh" or reags[1] == osadok:
         del reags[1]
         results.append(soed_2)
         kicked = 2
if reags[0] == "hoh" or reags[0] == osadok:
         del reags[0]
         results.append(soed_1)
         kicked = 1
soed_1 = reags[0]
soed_2 = reags[1]
soed_3 = reags[2]
if kicked == 4:
    del reags[0]
    results.append(soed_1)
if kicked == 3:
    del reags[1]
    results.append(soed_2)
if kicked == 2:
    del reags[1]
    results.append(soed_2)
if kicked == 1:
    del reags[2]
    results.append(soed_3)
print (reags[0], " + ", reags [1], " -> ", results[0], " + ", results[1])
