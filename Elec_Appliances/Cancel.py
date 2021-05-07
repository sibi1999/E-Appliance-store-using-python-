import random
import json
import smtplib
import smtplib
import pandas as pd


#a_file=open('data.json',"r")
#output=json.load(a_file)
#print(output.keys())
#a_file.close()
df = pd.read_csv('data.csv')
confirmed_ticket=pd.DataFrame(df)
#print(confirmed_ticket['name'])

#print(confirmed_ticket)
class Cancel_Ticket():

    def __init__(self,uname,password):
        self.uname=uname
        self.password=password

    @staticmethod
    def check_entry():
        print("Entered for Ticket cancelling")
        
    def generateotp(self):
        otp = random.randint(1111,9999)
        return otp


    def cancel_ticket(self):
        #a_file=open('data.json',"r")
        #output=json.load(a_file)
        #print(output.keys())
    
        print("hi")
        if self.uname in confirmed_ticket['name']:
            #data.drop(data.index[data['names'] == 'tom'])
            n=data[data.index[data['names']== self.uname]]
            print(n)
            print("otp sent")
            otp=self.generateotp()
            sender = 'assignment681@gmail.com'
            rec = 'assignmentuser597@gmail.com'
            password = 'assignment681!_'
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, rec, str(otp))
            print("please type the otp to confirm your request")
            check=int(input())
        
        
            #print(confirmed_ticket[uname].get('no_of_tickets'))
            if(otp==check):
                
                confirmed_ticket.pop(self.uname)
                print("Ticket Cancelled Sucessfully")
                pass
        
        a_file=open("data.json","w")
        json.dump(confirmed_ticket,a_file)
        a_file.close()



c=Cancel_Ticket("raju","123")
c.cancel_ticket()




