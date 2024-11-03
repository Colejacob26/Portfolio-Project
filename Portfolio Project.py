#Part 1
class ItemToPurchase:
    #Step 1
    #Default constructor with attribute names
    def __init__(self, item_name = "none", item_price = 0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity 
    
    def print_item_cost(self):
        print(self.item_name, self.item_quantity, "@", "$" + str(format(self.item_price,".2f")), "=", "$"+ str(format((self.item_price *self.item_quantity),".2f")))
    #Set up printing statement


item1 = ItemToPurchase()
item2 = ItemToPurchase() 
#Created Item #1 and #2 default

#Step 2
#Set Up
print("Please enter two items:")
print("Item #1")
print("Enter the item name:")
name1= input()

print("Enter the item price:")
price1= float(input())

print("Enter the item quantity:")
quantity1= int(input())
#Collects Data for Item #1


print("Item #2")

print("Enter the item name:")
name2= input()

print("Enter the item price:")
price2= float(input())

print("Enter the item quantity:")
quantity2= int(input())
#Copy and paste of Item #1 with item2 instered in


#assigns item 1 and 2 with the inputted attributes 
item1 =ItemToPurchase(name1,price1,quantity1)
item2 =ItemToPurchase(name2,price2,quantity2)

#Step 3
print("TOTAL COST")

item1.print_item_cost()
item2.print_item_cost()
print("Total:", "$"+ str(format(((item1.item_price*item1.item_quantity) + (item2.item_price * item2.item_quantity)),".2f")))
#Prints final costs 


################################
#Part 2

#Step 4 
class ShoppingCart:
    #Default Contructors
    def __init__(self, customer_name ='none', current_date = "January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
    cart_item = []


    #adding item
    def add_item(itp):
        cart.cart_item.append(itp)
        
        
    #removes item
    def remove_item(ItemName):
        for j in range(len(cart.cart_item)):
            if cart.cart_item[j].item_name == ItemName:
                #Remove description and item
                del dict1[cart.cart_item[j].item_name]
                del cart.cart_item[j]
                break
            
                

    #to modify description, price, quantity, does not work with default items
    def modify_item(itp):
        count2 = 0
        for j in range(len(cart.cart_item)):
            if ipt.item_name == cart.cart_item[j].item_name:
                count2 += 1
                if dict1[itp.item_name] == None and itp.item_price == 0 and item_quantity == 0:
                    print("Default Item")
                else:
                    print("Enter new description:")
                    dict1[itp.item_name] = str(input())
                    print("Enter new price:")
                    price2 = float(input())
                    print("Enter new quantity:")
                    quantity2 = int(input())
                    ItemToPurchase(itp.item_name, price2, quantity2)
            
        if count2 == 0:
            print("Item not found in cart")
    #To display no item in cart            


    #Total amount of items in cart
    def get_num_items_in_cart():
        total = 0
        for i in range(len(cart.cart_item)):
             total += cart.cart_item[i].item_quantity
        return total
        

    #Grand Total
    def get_cost_of_cart():
        total = 0
        for i in range(len(cart.cart_item)):
             total += cart.cart_item[i].item_price * cart.cart_item[i].item_quantity
        return total

    #prints all information besides description
    def print_total():
        #Check if shopping cart is empty
        if len(cart.cart_item) == 0:
            print("SHOPPING CART IS EMPTY")
            
        else:
            print(str(cart.customer_name) + "'s Shopping Cart", "-", cart.current_date)
            num = ShoppingCart.get_num_items_in_cart()
            print("Number of Items:", num)
            for i in range(len(cart.cart_item)):
                print(cart.cart_item[i].item_name, cart.cart_item[i].item_quantity, "@", "$" + str(format(cart.cart_item[i].item_price,".2f")), "=", "$" + str(format(cart.cart_item[i].item_price * cart.cart_item[i].item_quantity,".2f")))
                test = ShoppingCart.get_cost_of_cart()
            print("Total:", "$" + str(format(test,".2f")))
            

    #prints description
    def print_descriptions():
        print(str(cart.customer_name) + "'s Shopping Cart" , "-", cart.current_date)
        for i in range(len(cart.cart_item)):
            print(str(cart.cart_item[i].item_name) + ":", dict1[cart.cart_item[i].item_name])

#Step 5
#Menu
def print_menu(SC):
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    print("Choose an option:")
    print()
    option = input()




#Option A

    #Step 8
    if option == "a":
        print("Enter the item name:")
        name1 = str(input())

        print("Enter the item description:")
        dict1[name1] = str(input())

        print("Enter the item price:")
        price1= float(input())

        print("Enter the item quantity:")
        quantity1= int(input())
        
        item1 = ItemToPurchase(name1, price1, quantity1)
        ShoppingCart.add_item(item1)

#Option r
    #Step 9
    elif option == "r":
        print ("What item are you deleting?")
        remove = str(input())
        count = 0
        
        for i in range(len(cart.cart_item)):
            if str(cart.cart_item[i].item_name) == remove:
                count += 1
                ShoppingCart.remove_item(remove)
                break

        if count == 0:
            print("Item not found in cart")


#Option c
    #Step 10
    elif option =="c":
        print("Enter the item name:")
        count3 = 0
        name1 = input()
        for i in range(len(cart.cart_item)):
            if name1 == cart.cart_item[i].item_name:
                count3 +=1
                
                price2 = cart.cart_item[i].item_price
                
                print("Enter new item quantity:")
                
                quantity3= int(input())

                cart.cart_item[i] = ItemToPurchase(name1,price2,quantity3)
                    
        if count3 == 0:
            print("Item not found in cart")     
            

#Step 6
#Option i      
    elif option == "i":
        ShoppingCart.print_descriptions()

        
#option o
    elif option == "o":
        ShoppingCart.print_total()

            
#option q   
    elif option == "q":
        global quitCart
        quitCart = True


#Start of Main

#Step 7
#Collects Name and Date
print("Please enter your name:")
name = input()
print ("Please enter the date: (Example: January 1, 2020)")
date = input()

#Creates Shopping cart for the person who starts the code

print("Customer name:", name)
print("Today's date:", date)
cart = ShoppingCart(name,date)

dict1 = {} 

#Switch for the menu quitting 
quitCart = False
while quitCart == False:
    print_menu(cart)






