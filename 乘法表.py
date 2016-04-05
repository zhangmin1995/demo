for i in range(1,10):
    for j in range(i,10):
        formula = '{0:1}¡Á{1:1}={2: <2}'.format(i,j,i*j)
        print(formula,end=' ')
    print()
    count=1
    while(count<=i):
        print("       ",end=' ')
        count+=1 
