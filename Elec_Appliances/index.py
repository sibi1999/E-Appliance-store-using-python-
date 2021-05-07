import sys
sys.path.append(r'C:\Users\JARVIS\Desktop\mini_project_1\Elec_Appliances')

from ticket_booking import ticket_booking
from Cancel import Cancel_Ticket
import json

admin_data={'sibi':'123'}

cd=open('login_data.json',"r")
customer_data=json.load(cd)
cd.close()

a_file=open('data.json',"r")
output=json.load(a_file)
#print(output.keys())
a_file.close()


def admin_privileges():
    print()
    pc=open('product_count.json',"r")
    product_count=json.load(pc)
    pc.close()
    print("product","count")
    [print(i,j) for i,j in product_count.items()]
    print("\nDo You want to Change Values?\n")

    check=int(input("1 for yes and 0 for no"))
    while(check):
        print("which one do you need to change\n1.ironbox \n2.heater \n3.Charger")
        change=int(input())
        if(change==1):
            print("\n Give New Value for ironbox \n")
            n=int(input())
            product_count["ironbox"]=n
        elif(change==2):
            print("\n Give New Value for Heater\n")
            n=int(input())
            product_count["heater"]=n
        else:
            print("\n Give New Value for Charger\n")
            n=int(input())
            product_count["charger"]=n
            
            
        print("\nDo You want to Change Values?\n")
        check=int(input("1 for yes and 0 for no"))
    [print(i,j) for i,j in product_count.items()]
    pc=open("product_count.json","w")
    json.dump(product_count,pc)
    pc.close()

    

def admin_login():
    print("Please typer Your Username")
    admin_username=input().strip()
    password=input("\nPlease Enter Your Password\n").strip()
    if(admin_username in admin_data and admin_data[admin_username]==password):
        admin_privileges()
    else:
        print("Sorry Wrong password or Username")
        


def login_page():
    print("If Admin press 1 or Customer press 2")
    check=int(input())
    if(check==1):
        admin_login()
    else:
        customer_login()


def customer_login():
    print("new user(1) or existing user(2)")
    
    check=int(input())

    if(check==1):
        print("give urself a username")
        uname=input().strip()
        print("give urself a password")
        password=input().strip()
        customer_data[uname]=password
        customer=ticket_booking(uname,password)
        customer.create_ticket()
    else:
        
        print("Please enter Your Username")
        uname=input().strip()
        print("password")
        password=input().strip()
        
        if uname in customer_data and customer_data[uname]==password:
            print("*********************************************************************")
            print("\t1.Buy a product")
            print("\t2.Cancel Ticket ")
            print("\t3.Check Availability")
            print("\t4.View Ticket")
            print("\t5.Exit")
            print("\n ********************************************************************")
            print("\npls enter a key")
            check=int(input())

            if(check==1):
                customer=ticket_booking(uname,password)
                customer.create_ticket()
            elif(check==2):
                customer=Cancel_Ticket(uname,password)
                customer.cancel_ticket()
            elif(check==3):
                customer=ticket_booking(uname,password)
                customer.check_availability()
            elif(check==4):
                customer=ticket_booking(uname,password)
                customer.view_ticket()
            else:
                print("\nThank You")
                exit()
                
        else:
            print("Wrong Username or Password")
            



while True:
    print("\t E-Electronic Appliance store")
    print()
    login_page()
   
   
    cd=open("login_data.json","w")
    json.dump(customer_data,cd)
    cd.close()

    
    
    print("\n\tdo you want to continue 1.yes 2.No")
    check=int(input())
    if(check==2):
        break


