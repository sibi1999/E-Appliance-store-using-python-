import sys
import mysql.connector
import smtplib
import smtplib

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345sibi",
  database="eapp"
)

mycursor = mydb.cursor()

#mycursor.execute("select * from customer_table")
#for x in mycursor:
 # print(x)

  
sys.path.append(r'C:\Users\JARVIS\Desktop\mini_project_1\Elec_Appliances')

from datetime import date

from product import ironbox,Electric_heater,Charger
import json
import pandas as pd

#a_file=open('data.json',"r")
#output=json.load(a_file)
#print(output.keys())
#a_file.close()
df = pd.read_csv('data.csv')
df=pd.DataFrame(df)
#print(df)
#confirmed_ticket={}
#df=pd.DataFrame({})

class ticket_booking():
    
    def __init__(self,uname,password):
        self.uname=uname
        self.password=password
        
    @staticmethod
    def check_entry():
        print("Entered for Ticket Booking")
    
    def create_ticket(self):
        print("\tHola Customers ")

        p=0
        while(True):
        #print(movie_list)
            
            print("Hello "+self.uname+" "+ "Which product do You want to purchase")
            print("\n\t 1.Ironbox")
            print("\n\t 2.Heater")
            print("\n\t 3.Charger")
            print()
            print("\n press any one key to proceed\t")
            print()

            n=int(input())
            region=["chennai","banglore","mumbai"]
            print("Please enter the region You belong to")
            for i in region:
                print(i,end=" ")
            region=input("Enter the region ")


            if (n==1):
                i=ironbox()
                p_id=i.details()
                
                
                

                print("\n Please enter the colour You want ")
                print("\n The Colours we have are ")
                print("\t1.red \t2.blue")
                ccode=int(input())
                i.colour_code()
                no=int(input("Enter the number of ironbox You need"))
                check=i.check_availability(no)
                if(check==0):
                    print("Stock Unavailable")
                else:
                    p+=100
                    #cart["ironbox"]=no
                    cart="ironbox"
                    i.deduct_tickets(no)
                    print("Added To cart")
            elif(n==2):
                e=Electric_heater()
                p_id=e.details()
                print("\n Please enter the colour You want ")
                print("\n The Colours we have are ")
                print("\t1.red \t2.blue")
                ccode=int(input())
                e.colour_code()
                
                no=int(input("Enter the number of heater You need"))

                check=e.check_availability(no)

                if(check==0):
                    print("Stock Unavailable")
                else:
                    p+=200
                    #cart["ironbox"]=no
                    cart="heater"
                    e.deduct_tickets(no)
                    print("Added To cart")
  
                
                #cart.append("Heater")
            else:
                c=Charger()
                p_id=c.details()
                p+=50
                #cart.append("Charger")
            #print("Do You want to continue?? 1 for Yes 0 for NO\n")
            #x=int(input())
            #if not x:
                #break
            
                
            if(self.confirmation(p*no,cart,no,region,p_id)):
                continue
            else:
                return 0
        
        
    def ticket_print(self,user_data):
        print()
    
        print()
        self.confirmed_ticket={'name':[user_data[0]],'product':[user_data[2]],'price':[user_data[1]],'region':[user_data[4]],'quantity':[user_data[3]],'date':[date.today()]}
        print("Thank You")
        final_tuple=(user_data[0],user_data[2],user_data[1],user_data[4],user_data[3],date.today(),user_data[5])
        mycursor = mydb.cursor()

        sql = "INSERT INTO customer_table (name, product,price,region,quatity,date,product_id) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = final_tuple
        mycursor.execute(sql, val)

        mydb.commit()
        print()

   

   

    def confirmation(self,price,cart,no,region,p_id):
            print("R u sure to proceed with payment of rupees",price)
            user_data=(self.uname,price,cart,no,region,p_id)
            print("Final Confirmation y or n")
            check=input().strip()
            if(check=='y'):
                self.ticket_print(user_data)
            else:
                print("Ok Thank u")
                exit()
        
            #a_file=open("data.json","w")
            #json.dump(confirmed_ticket,a_file)
            #a_file.close()

            print(self.confirmed_ticket)
            
            output= pd.DataFrame(self.confirmed_ticket)
        
            global df
            df=df.append(output,ignore_index=True)
            #print(df)
            
            #output.to_csv(r'C:\Users\JARVIS\Desktop\mini_project_1\Elec_Appliances\data.csv',index=False)
            #a_file=open("data.csv","w")
            df.to_csv(r'C:\Users\JARVIS\Desktop\mini_project_1\Elec_Appliances\data.csv',index=False)

            print("\n")
            
            #mycursor.execute("select * from customer_table")
            #for x in mycursor:
                #print(x)

            sender = 'assignment681@gmail.com'
            rec = 'assignmentuser597@gmail.com'
            password = 'assignment681!_'
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender, password)
            msg="Your order has been placed "+user_data[0]
            server.sendmail(sender, rec,msg)

            print("Do You want to continue shopping ?? 1 for Yes 0 for NO\n")
            x=int(input())
            if x==0:
                return None
            else:
                return 1
            
            #a_file.close()
            



    def view_ticket(self):
        if self.uname in confirmed_ticket:
            print(self.uname)
            print(confirmed_ticket[self.uname])

#t=ticket_booking("kamal hassan","123")
#t.create_ticket()




