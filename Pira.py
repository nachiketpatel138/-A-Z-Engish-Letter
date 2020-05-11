for row in range(4):
    for col in range(7):
        if row==3:
            print('*',end='')
        elif row==2 and (col>0 and col<6) or row==1 and (col>1 and col<5) or row==0 and (col>2 and col<4):
            print('*',end='')
        else:
            print(end=' ')
    print()