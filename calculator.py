while True:
    print('select operation')
    print('1. Addition')
    print('2. Subraction')
    print('3. Multipication')
    print('4. division')
    choice=int(input('enter operation number'))
    n1,n2=map(float,input('enter two numbers').split())
    if choice==1:
        print('addition is ',n1+n2)
    elif choice==2:
        print('sub is ',n1-n2)
    elif choice==3:
        print('mul is ',n1*n2)
    elif choice==4:
        if n2 != 0:
            print('div is ',n1/n2)
        else:
            print('div is not possible')
    else:
        print('select correct operation')
