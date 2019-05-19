from database import accountlist as smry
def details():
    while 1:
        id = int(input("Enter the account number (1 for entire list,0 to exit) : "))
        if id==0:
            break
        elif id==1:
            for key in smry.keys():
                print (' {}   {}   {}'.format(key,smry[key][0],smry[key][1]))
        elif id in smry.keys() :
                    print ('Name: {}   Balance : {} '.format(smry[id][0],smry[id][1]))
                    