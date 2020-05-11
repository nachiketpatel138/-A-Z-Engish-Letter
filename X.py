i=0
j=4
for row in range(5):
    for col in range(5):
        if row==i and col==j:
            i=i+1
            j=j-1
            print('*',end='')

        elif row==col:
            print('*',end='')
        else:
            print(end=' ')
    print()