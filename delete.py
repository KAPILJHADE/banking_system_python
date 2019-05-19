def delete_account():
    from database import accountlist as al
    while 1:
        value=int(input('Enter account number'))
        if value in al.keys():
            print('Name: {}  Balance: {}'.format(al[value][0],al[value][1]))
            ch=input(' Confirm Closing of Account? (yes/no): ')
            if ch=='yes':
                del al[value]     
            else: 
                print(' Account is not Closed')
        else:
            print('\n Account does not exist')
        choice=input(' Do you want to close more accounts? (yes/no): ')
        if choice!='yes':
            break