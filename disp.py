from database import accountlist as al
def display():
     print('Account Number','Name','Balance')
     for key in al.keys():
         print (' {}   {}   {}  '.format(key,al[key][0],al[key][1]))