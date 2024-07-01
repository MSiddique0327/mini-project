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
   