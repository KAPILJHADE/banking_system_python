from add import add_account as a
from delete import delete_account as d
from disp import display as l 
from banking import accounting as acc 
from deposit import depositing as dep
from summary import details as s
while 1:
    print('\n\n\n     Welcome to IIIT DHARWAD BANK ')
    print('\n\t Select your choice')
    print('\n 0. Account Summary \n 1. All account details \n 2. cash withdrawl \n 3. cash deposit \n 4. Add account \n 5. delete account \n 6. Exit')
    ch=int(input(' \n Enter your choice : '))
    if ch==0:
        s()
    elif ch==1:
        l()
    elif ch==2:
        acc()
    elif ch==3:
        dep()
    elif ch==4:
        a()
    elif ch==5:
        d()
    elif ch==6:
        break
    else:
        print(' \n Wrong Choice!')