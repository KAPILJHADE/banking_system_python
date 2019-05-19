from database import accountlist as acc 
def add_account():
    code=int(input("\nchoose any 10 digit account number : "))
    if code not in acc.keys():
        Name=input("Enter your name : ")
        Balance=float(input("Enter initial account balance you wish to deposit:"))
        acc.update({code:[Name,Balance]})
    else:
        print('The account number already exists')