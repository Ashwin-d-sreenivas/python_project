import mysql.connector as m1
cn=m1.connect(host='localhost', user='root', passwd='root',database='csproject')
if cn.is_connected():
    print("Connection Established!")
else:
    print("\nConnection Error... Kindly Check!")


cur=cn.cursor()
cur.execute("create table if not exists item(sno int,name varchar(50),price int,quantity int);")
cn.commit()
print("Table successfully created!\n")

print("********SHOP REGISTER********")


def additem():


    while True:
        sno=int(input("Enter Serial Number: "))
        name=input("Enter item Name: ")
        price=int(input("Enter price of Item: "))
        quantity=int(input("Enter quantity of Item: "))
        cur=cn.cursor()
        cur.execute("insert into item values(%s,%s,%s,%s);",(sno,name,price,quantity))

        ch=int(input("\n1. CONTINUE ENTERING VALUES \n2. STOP ENTERING VALUES\n:"))
        if ch==1:
            continue
        elif ch==2:
            break
        else:
            print("ENTER VALID ARGUMENT!")




def deleteitem():
    
    while True:
        
        cur=cn.cursor()
        serno=int(input("Enter Serial Number: "))
        ch1=int(input("\n1. CONFIRM DELETION\n2 .GO BACK\n:"))
        if ch1==1:
            cur.execute("delete from item where sno=%s;",(serno,))
            print("Item deleted successfully!")
        elif ch1==2:
            print("No item deleted!")
        else:
            print("ENTER VALID ARGUMENT!")

        ch2=int(input("\n1. CONTINUE DELETING VALUES\n2. STOP DELETING VALUES\n:"))
        if ch2==1:
            continue
        elif ch2==2:
            break
        else:
            print("ENTER VALID ARGUMENT")




def updateitem():
    print("********RECOMMEND TO DISPLAY FIRST TO KNOW EXACT VALUES BEFORE UPDATING********\n")

    while True:

        
        cur=cn.cursor()
        serno1=int(input("Enter Serial number of item which needs to be update: "))
        print("\n********Change the values only if there is change. If no change in value put current value********")
        name1=input("Enter Updated name: ")
        price1=int(input("Enter Updated price: "))
        quantity1=int(input("Enter Updated quantity: "))
        ch3=int(input("\n1. CONFIRM UPDATION\n2. GO BACK\n:"))
        if ch3==1:
            cur.execute("update item set name=%s,price=%s,quantity=%s where sno=%s;",(name1,price1,quantity1,serno1))
            print("Item updated successfully!")
        elif ch3==2:
            print("No item Updated!")
        else:
            print("ENTER VALID ARGUMENT!")

        ch4=int(input("\n1. CONTINUE UPDATING VALUES\n2. STOP UPDATING VALUES\n:"))
        if ch4==1:
            continue
        elif ch4==2:
            break
        else:
            print("ENTER VALID AGUMENT!")
            
                    


def displayitem():
    
    cur=cn.cursor()
    cur.execute("select* from item;")
    data=cur.fetchall()
    for i in data:
        print(i)
        
               





#FINAL CHOICE
while True:
    choice=int(input("\n1. INSERT VALUES\n2. DELETE\n3. UPDATE\n4. DISPLAY\n5. EXIT\n: "))
    if choice==1:
        additem()
        cn.commit()
        print("Values added successfully!")
    elif choice==2:
        deleteitem()
        cn.commit()
        print("Values changed successfully!")
    elif choice==3:
        updateitem()
        cn.commit()
        print("Values updated successfully!")
    elif choice==4:
        print("(S.NO,NAME,PRICE,QUANTITY)\n             \n***********************\n               ")
        displayitem()
    elif choice==5:
        print("EXITING...")
        break

    
    
                    
                

                    
          
           
        
            
            
                               
