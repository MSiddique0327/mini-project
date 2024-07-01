print( "Welcome to the Supermart inventory management system")

inventory={
    "Oreo": {"price":40, "count":100},
    "Colgate": {"price":20, "count":80},
    "Lays": {"price":30, "count":50},
    }

def add_item():
   name=input("Enter the name of the item: ")
   price=int(input("Enter the price of the item: "))
   count=int(input("Enter the count of the item: "))
   inventory[name]={"price":price, "count":count}
   return print(inventory)

def buy_item():
    name=input("Enter the name of the item: ")
    count=int(input("Enter the count of the item: "))
    if name in inventory:
        if inventory[name]["count"]>=count:
            inventory[name]["count"]-=count
            print("Item purchased successfully")
        else:
            print("we don't have enough stock")

def change_price():
     name=input("Enter the name of the item:")
     price=int(input("Enter the new price of the item:"))
     for key , values in inventory.items():
          if key==name:
               inventory[key]["price"]=price
               print("Price updated successfully")
               break
          else:
               print("Item not available")
               exit()
