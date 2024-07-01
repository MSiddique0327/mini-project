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

def update_inventory():
     name=input("Enter the name of the item:")
     count=int(input("Enter the new count of the item:"))
     for key , values in inventory.items():
          if key==name:
               inventory[key]["count"]=count
               print("Count updated successfully")
               break
          else:
               print("item not available")
               exit()

def display_inventory():
     total_sale=0
     print("Inventory:")
     for key , values in inventory.items():
          print(f"{key} : {values['count']}")
          total_sale+=values['price']*values['count']
          print(f"Total sales: {total_sale}")

def main():
    while True:
        print("1. Add an item to the inventory.")
        print("2. Buy an item from the inventory.")
        print("3. Change the price of an existing item in the inventory.")
        print("4. Update the inventory of an existing item in the inventory.")
        print("5. Display the inventory.")
        print("6. Exit the program.")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("invalid input Plz enter a number")
            continue

        if choice == 1:
            add_item()
            
            continue
        elif choice == 2:
            buy_item()
            
            continue
        elif choice == 3:
            change_price()
            
            continue
        elif choice == 4:
            update_inventory()
            
            continue
        elif choice == 5:
            display_inventory()
            
            continue
        else:
             if choice == 6:
                 
                 continue
print(inventory)
main()