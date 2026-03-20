def CheckPrime(Brr):

    Prime =[]

    for i in Brr:

        if( i < 2):
            continue
        
        for no in range(2,int(i/2) + 1):
                if(i%no == 0):
                    break
        else:
             Prime.append(i)
        
    return Prime
