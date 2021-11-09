a=input().split('/')
if len(a)==3:
    b=0
    glas='аоуэиеёюяы'
    d=1
    for i in range(len(a)):
        for j in a[i].lower():
            if j in glas:
                b+=1
        if i==0 or i==2:
            if b!=5:
                d=0
                print('Не хайку.');break
        elif i==1:
            if b!=7:
                d=0
                print('Не хайку.');break


        b=0 # нужно каждый раз посчитать с нуля
    if d==1:
        print('Хайку!')
        
else:print('Не хайку. Должно быть 3 строки.')  
