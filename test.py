

mylist = [[0]*10 for _ in range(10)]
print(mylist)

for row in mylist:
    if not all([row[0] == row[i] for i in range(3)]):
        print("row not equal")
        

for i in range(3):
    if not all([mylist[0][i] != mylist[j][i] for j in range(3)]):
        print("cols not equal")