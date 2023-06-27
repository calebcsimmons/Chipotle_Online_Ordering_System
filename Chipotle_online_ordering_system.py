 #? Class Based Chipotle Online Ordering System:
 
class Burrito: # class named Burrito to take specified arguments 
    def __init__(self, meat, to_go, rice, beans, extra_meat = False, guacamole = False, cheese = False, pico = False, corn = False) -> None:
        
        self.meat = meat if meat in ["chicken", "pork", "steak", "tofu"] else False
        self.to_go = to_go if to_go == True else False
        self.rice = rice if rice == "brown" or rice =="white" else rice == False
        self.beans = beans if beans == "black" or beans == "pinto" else beans == False
        self.extra_meat = extra_meat if extra_meat==True else False
        self.guacamole = guacamole if guacamole==True else False
        self.cheese = cheese if cheese==True else False
        self.pico = pico if pico==True else False
        self.corn = corn if corn==True else False
    
    #Defining setters to reassign arguments and ensure their validity    
    def set_meat(self, meat): 
        meatval = ["chicken", "pork", "steak", "tofu", False]
        if meat in meatval:
            self.meat = meat
        else:
            self.meat = False  

    def set_to_go(self, to_go):
        if to_go == True:
            self.to_go = to_go
        else:
            self.to_go = False      
        
    def set_rice(self, rice):
        if rice == "brown" or rice == "white":
            self.rice = rice
        else:
            self.rice = False
         
    def set_beans(self, beans):
        if beans == "black" or beans == "pinto":
            self.beans = beans
        else:
            self.beans = False
        
    def set_extra_meat(self, extra_meat):
        if extra_meat == True:
            self.extra_meat = extra_meat
        else:
            self.extra_meat = False

    def set_guacamole(self, guacamole):
        if guacamole == True:
            self.guacamole = guacamole
        else:
            self.guacamole = False
        
    def set_cheese(self, cheese):
        if cheese == True:
           self.cheese = cheese
        else:
            self.cheese = False
        
    def set_pico(self, pico):
        if pico == True:
           self.pico = pico
        else:
            self.pico = False
        
    def set_corn(self, corn):
        if corn == True:
            self.corn = corn
        else:
            self.corn = False
    
    #Defining getters     
    def get_meat(self):
        return self.meat
     
    def get_to_go(self):
        return self.to_go
    
    def get_rice(self):
        return self.rice
    
    def get_beans(self):
        return self.beans
    
    def get_extra_meat(self):
        return self.extra_meat
    
    def get_guacamole(self):
        return self.guacamole    
      
    def get_cheese(self):
        return self.cheese   
    
    def get_pico(self):
        return self.pico
    
    def get_corn(self):
        return self.corn

    def get_cost(self): #Calculating cost of a burrito based on given arguments
        cost = 5
        if self.meat == "chicken" or self.meat == "pork" or self.meat == "tofu":
            cost +=1
        if self.meat == "steak":
            cost +=1
        if self.extra_meat and self.meat != False:
            cost +=1
        if self.guacamole:
            cost +=0.75
        cost == float(cost)
        return cost

def receipt(burrito_list): #Function for calculating receipt for any/all burritos purchased
    cost = 0
    for burrito in burrito_list:
        print(burrito.get_meat() + " " + burrito.get_rice() + " rice burrito = $" + str(burrito.get_cost()))
        cost += burrito.get_cost()
    tax = round(0.09 * cost,2)
    print("Tax: $" + str(tax))
    total = tax + cost
    return "Total: $" + str(total)

#Testing Code
burrito_1 = Burrito("tofu", True, "white", "black")
burrito_2 = Burrito("steak", True, "white", "pinto", extra_meat = True)
burrito_3 = Burrito("pork", True, "brown", "black", guacamole = True)
burrito_4 = Burrito("chicken", True, "brown", "pinto", extra_meat = True, guacamole = True)
burrito_list = [burrito_1, burrito_2, burrito_3, burrito_4]
print(receipt(burrito_list))



