for row in range(7):
    for col in range(5):
        if (col==0) or (row==0 or row==6) or (col==4 and(row>2 and row<7)) or (row==3  and col>1 ) :
            print('*' ,end='')
        else:
            print(end=' ')
    print()