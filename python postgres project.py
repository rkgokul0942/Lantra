def view_menu():
    view_menu=("select item_name,price,category from Items")
    cursor.execute(view_menu)
    rows = cursor.fetchall()
    for i in rows:
        print(f"Item_Name = {i[0]}")
        print(f"Price {i[1]}")
        print(f"Category = {i[2]}\n")


def order():
    view_menu()
    print("\n\nYour order plz")
    while True:
        ordered_item=input("\nItem name (eg:idly) : ").upper()
        ordered_quantity=int(input("Quantity : "))
        if ordered_item in rows:
            next=input("\n'ENTER' to continue || 'DONE' to place order :  ").upper()
            orders=(table_number,ordered_item,ordered_quantity)
            ordered_list.append(orders)
            
        if (next == "DONE"):
            print("Your order has been placed :)")
            break

        else:
            print("Please check our menu and Enter valid Item")


    dining()

def again():
    print("Add items to your order list :)")
    print("\n\nYour order plz")
    while True:
        ordered_item=input("\nItem name (eg:idly) : ").upper()
        ordered_quantity=int(input("Quantity : "))
        if ordered_item in rows:
            next=input("\n'ENTER' to continue || 'DONE' to place order :  ").upper()
            orders=(table_number,ordered_item,ordered_quantity)
            again_ordered.append(orders)
        if (next == "DONE"):
            print("Your order has been placed :)")
            break

        else:
            print("Please check our menu and Enter valid Item")

    adddining()
    print("Added successfully")

def dining():
    for i in ordered_list:
        query=(f"insert into dining (table_no,items,quantity) values {i};")
        cursor.execute(query)
def adddining():
    for i in again_ordered:
        query=(f"insert into dining (table_no,items,quantity) values {i};")
        cursor.execute(query)

        

def chef():
    chef_id=int(input("Enter your chef ID : "))
    if (chef_id ==123)or(chef_id ==456)or(chef_id ==789):
        chef_Tnumber=int(input("\nCheck orders on Table_number : "))
        query=(f"select * from dining where dining.table_no = {chef_Tnumber}")
        cursor.execute(query)
        rows = cursor.fetchall()
        for i in rows:
            table=i[0]
            items=i[1]
            quantity=i[2]
            print("Table_ID =",table)
            print("Item_Name =",items)
            print("Quantity =",quantity)
        while True:
            served=input("\nOrders Served : ").upper()
            for i in rows:
                if served==rows[1]:
                    query1=(f"delete from dining where table_no = {chef_Tnumber} and items = {served}")
                    query2=(f"Insert into bill(table_no,items,quantity) values ({table},{items},{quantity})")
            if served=="DONE":
                break



        

    else:
        print("Invalid Chef ID")  

def cancellation():
    in_=int(input("To cancel an Item [1] \nEdit Item Quantity [2]  :  "))
    if in_==1:
        del_item=input("Enter the item to be cancelled : ").upper()
        query=(f"delete from dining where items ='{del_item}' and table_no={table_number}") 
        print("Item Cancelled")
    else:
        alt_item=input("Enter the item name : ").upper()
        qua=int(input("Quantity : "))
        query=(f"update dining set quantity = {qua} where items = '{alt_item}' and table_no = {table_number}")
        print("Order Edited Successfully")
    cursor.execute(query)

def fetchItems():
    fetItems=("select item_name from Items")
    cursor.execute(fetItems)
    fetItem = cursor.fetchall()
    

import psycopg2
ordered_list=[]
again_ordered=[]
rows=["IDLY","VADA","DOSA","POORI","VEN PONGAL","CHICKEN BIRIYANI","MUTTON BIRIYANI","CHICKEN CHILLI","PAROTTA","MUTTON CHUKKA"]
conn = psycopg2.connect(database="Hotel_orders",user="postgres",password="12345")
print("\n(((: ----- We Heartly Welcome you to experience our Traditional Taste  ----- :)))") 
cursor= conn.cursor()
who=input("CHEF / CUSTOMER : ").upper()
if who=="CUSTOMER":
    table_number=int(input("\nEnter your Table_Number [1,2,3,4,5]: "))
    entry=input("\nWould you like to place your order now ? YES/LATER : ").upper()
    if (entry == "YES"):
        order()
    else:
        print("We are awaiting to take you to the world of taste")
        press=input("press ENTER to take your order  ")
        order()
    help=input("To ADD OR CANCEL order : ").upper()
    if help=="ADD":
        again()
    if help=="CANCEL":
        cancellation()
    print("Your Order is being prepared ")
    print("\nThank You")
conn.commit()
if who=="CHEF":
    chef()
conn.close()