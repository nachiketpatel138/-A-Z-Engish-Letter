i=0
j=4
for row in range(6):
    for col in range(5):
        if (col==row and row<3) :
            print('*',end='')
        elif row==i and col==j:
            print('*',end=' ')
            i+=1
            j-=1     
        elif col==2 and row>2:
            print('*',end='')
        else :
            print(end=' ')
    print()