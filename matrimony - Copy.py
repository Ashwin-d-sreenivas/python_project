import mysql.connector as sqlcon

con = sqlcon.connect(host="localhost", user="root",passwd="", database="MATRIMONYSITE")
if con.is_connected()==False:
        print("Error connecting to MySQL database")
else:
    c1=con.cursor( )
    c1.execute("create table IF NOT EXISTS user_id(user_name varchar(55) UNIQUE,password varchar(55),client_i_d int)")
     
while True:
        print('1.NEW USER REGISTRATION')
        print('2.EXISTING USERS')
        n=int(input('Enter your choice:'))
        if n==1:
                
                c1=con.cursor( )
                c1.execute("select * from user_id")
                rows=c1.fetchall()
                nrows=c1.rowcount
                
                name=input('Enter your  User name:')
                passwd=int(input('Enter  your  Password(only numbers):'))
                               
                c1.execute("INSERT  INTO user_id  values (%s,%s,%s)",(name,passwd,nrows+1))
                con.commit()
                print()
                print('USER created succesfully ')
                print("Your client id is :-  ",nrows+1)
        if n==2:
                name=input('Enter your Username=')
                print()
                passwd=int(input('Enter your  Password='))
                c1.execute("select * from user_id where password=%s and user_name=%s",(passwd,name))
                if c1.fetchall() is  None:
                        print()
                        print('Invalid username or password')
                         
                print('1.LOGIN')
                print('2.update')
                print('3.delete')
                print('4.Exit')
                n=int(input('Enter your choice:'))
                if n==1:
                        
                        
                        c2=con.cursor()
                        c2.execute("create table  IF NOT EXISTS client_details (client_I_D int primary key,name varchar(100),address varchar(100),gender varchar(10),caste varchar(50),appearence varchar(100),age int(4),profession varchar(65),phone_no int)")
                        print("Enter details")
                        client_I_D=int(input('enter client i.d:'))
                        name=input("Enter name")
                        address=input("Enter residential address")
                        gender=input('enter gender')
                        caste=input('enter caste')
                        appearence=input("Enter appearance")
                        age=int(input("Enter age"))
                        profession=input("Enter profession")
                        phone_no= int(input("Enter phone number"))
                        c2.execute("insert into client_details values (%s, %s, %s, %s, %s, %s,%s,%s,%s)",(client_I_D,name,address,gender,caste,appearence,age,profession,phone_no))
                        print("\nData inserted successfully\n")
                        con.commit( )
                
                elif n==2:
                        c3=con.cursor()
                        client_i_d=int(input('enter id to be updated:'))
                        print("Which data is to be modified")
                        print("1 for Name change")
                        print("2 for Address change")
                        print("3 for Caste change")
                        print("4 T Gender change")
                        print("5 for Appearence change")
                        print("6 for Age change")
                        print("7 for Profession change")
                        print("8 for Phone number change")
                        op=int(input("Enter option"))
                        if op==1:
                                name=input('enter modified name')
                                c3.execute("update client_details set name=%s where client_i_d=%s",(name,client_i_d))
                        if op==2:
                                address=input("Enter modified residential address")
                                c3.execute("update client_details set address=%s where client_i_d=%s",(address,client_i_d))
                        if op==3:
                                caste=input('enter caste')
                                c3.execute("update client_details set caste=%s where client_i_d=%s",(caste,client_i_d))
                        if op==4:
                                gender=input('enter gender:')
                                c3.execute("update client_details set caste=%s where client_i_d=%s",(gender,client_i_d))
                        if op==5:
                                appearence=input('enter appearence')
                                c3.execute("update client_details set caste=%s where client_i_d=%s",(appearence,client_i_d))
                        if op==6:
                                age=int(input('enter age'))
                                c3.execute("update client_details set age=%s where client_i_d=%s",(age,client_i_d))
                        if op==7:
                                profession=input('enter profession')
                                c3.execute("update client_details set age=%s where client_i_d=%s",(profession,client_i_d))
                        if op==8:
                                phone_no=int(input('enter phone number'))
                                c3.execute("update client_details set =%s where client_i_d=%s",(profession,client_i_d))
                
                        
                        print("\nData updated successfully\n")
                        con.commit( )
                elif n==3:
                        c4=con.cursor()
                        c4.execute("select * from client_details")
                        print("\n")
                        data = c4.fetchall()
                        print("The different user id's are ...")
                        for i in data:
                                print(i[0])
                        client_i_d=int(input('i_d to be deleted:'))
                        c4.execute("delete from client_details where client_I_D=%s",(client_i_d,))
                   
                        con.commit()
                elif n==5:
                        print("Logging out")
                        break
        
                        
        
con.close( )    
