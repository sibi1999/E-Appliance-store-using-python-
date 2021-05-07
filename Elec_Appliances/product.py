import os
os.chdir(r"C:\Users\JARVIS\Desktop\mini_project_1\Elec_Appliances")


import sys
sys.path.append(r'C:\Users\JARVIS\Desktop\mini_project_1\Elec_Appliances')

from abc import ABC,abstractmethod

import json
pc=open('product_count.json',"r")
output=json.load(pc)
#print(output.keys())
pc.close()

class product(ABC):
    @abstractmethod
    def details(self):
        pass
    @abstractmethod
    def colour_code(self):
        pass

    @abstractmethod
    def check_availability(self):
        pass
class ironbox(product):

    def details(self):
        print("\n The price of the iron box is 100")
    def colour_code(self):
        print("colour Ok")
    def check_availability(self,n):
        #print("Entered CA")
        self.available=output["ironbox"]
        #print(self.available,n,self.available < n)
        if(self.available < n):
            return 0
        else:
            return 1
    def deduct_tickets(self,n):
        output["ironbox"]-=n
        pc=open('product_count.json',"w")
        json.dump(output,pc)
        pc.close()
        
        

class Electric_heater(product):
    
    def details(self):
        print("\n The price of the heater is 200")
    def colour_code(self):
        print("colour Ok")
    def check_availability(self,n):
        #print("Entered CA")
        self.available=output["heater"]
        print(self.available,n,self.available < n)
        if(self.available < n):
            return 0
        else:
            return 1
    def deduct_tickets(self,n):
        output["heater"]-=n
        pc=open('product_count.json',"w")
        json.dump(output,pc)
        pc.close()

class Charger(product):
    
    def details(self):
        print("\n The price of the charger is 50")
    def colour_code(self):
        print("colour Ok")
    def check_availability(self,n):
        #print("Entered CA")
        self.available=output["charger"]
        print(self.available,n,self.available < n)
        if(self.available < n):
            return 0
        else:
            return 1
    def deduct_tickets(self,n):
        output["charger"]-=n
        pc=open('product_count.json',"w")
        json.dump(output,pc)
        pc.close()


#c=ironbox()
#c.details()
#print(c.check_availability(5))

#i=ironbox()
#i.deduct_tickets(5)

