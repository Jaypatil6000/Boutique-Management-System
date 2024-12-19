import mysql.connector # type: ignore
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="boutique"
     )

mycursor = mydb.cursor()

print("Welcome to Boutique Management System")

print("Please select your role:")
print("1. Customers")
print("2. Employees")
print("3. Employer")

choose = input("Enter the number and your role (1/2/3): ")

user = input("Please enter your username: ")
pas = input("Please enter your password: ")

if user == "jay" and pas == "1728":
        print("Login successful!.")
else:
        print("Please try again.")
        exit()

if choose == '3' or choose == 'Employer':
    print("Welcome to the Employer")
    
    if choose =='3' or choose == 'Employer':
        print("1.add product\n2.view product\n3.add Employees\n4.view Employees\n5.delete Employees")
        choice=input("choose the one option")
    else:
        print("select the wrong option")    
        exit()

    if choice == '3':
     print("Detail of Employees")
                
     b = input("Enter your Name: ")
     c = input("Enter your User_Id:")
     d = input("Enter your Password: ")
     f = input("Enter your Gender:")

    
     sql = "INSERT INTO employer (Name, User_Id, Password, Gender) VALUES( %s, %s, %s, %s)"
     value =(b, c, d, f) 
     mycursor.execute(sql, value)
     mydb.commit() 

     print("Succesfully Add Employees")
    
    elif choice == '4':
        print("view employees")
        
        mycursor.execute("select*from employer")
        rd = mycursor.fetchall()
        for t in rd:
            print(t)
            
    if choice == '5':
        print("delete Employees")     
        
        sql = "DELETE FROM employer WHERE name = 'aayush'"
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")
        
    if choice == '1':
        print("add product")
        
        c = input("Enter your Product_name:")
        d = input("Enter you size: ")
        f = input("Enter your Colour:")

        
        sql = "INSERT INTO product (Product_name,size, Colour) VALUES(%s, %s, %s)"
        value =(c, d, f) 
        mycursor.execute(sql, value)
        mydb.commit() 

        print("Succesfully Add Product")
        
    elif choice == '2':
        print("view product")
        
        mycursor.execute("select*from product")
        rd = mycursor.fetchall()
        for x in rd:
            print(x)    
            
if choose == '2' or choose == 'Employees':
    print("Welcome to the Employees")            
    
    if choose =='2' or choose == 'Employees':
        print("1.updating delivered orders of customers\n2.add new product\n3.deleting a product")
        choice=input("choose the one option")
    else:
        print("select the wrong option")    
        exit()
        
    if choice == '1':
        print("updating delivered orders")
        
        
       
        



    if choice == '2':
        print("add new product")
        
        a = input("Enter your Product_name:")
        b = input("Enter you size: ")
        c = input("Enter your Colour:")

        
        sql = "INSERT INTO product (Product_name,size, Colour) VALUES(%s, %s, %s)"
        value =(a, b, c) 
        mycursor.execute(sql, value)
        mydb.commit() 

        print("Succesfully Add Product")
        
    if choice == '3':
        print("deleting a product")     
        
        sql = "DELETE FROM product WHERE product_name = 'socks'"
        mycursor.execute(sql)
        mydb.commit()
        print("Succesfully deleting Product")    
        
if choose == '1' or choose == 'Customers':
    print("Welcome to the Customers")            
    
    if choose =='1' or choose == 'Customers':
        print("1.book order\n2.view booking\n3.delete booking\n4.update booking")
        choice=input("choose the one option")
    else:
        print("select the wrong option")    
        exit()        
       
    if choice == '1':
        print("book order")
        
        mycursor.execute("select*from product")
        rd = mycursor.fetchall()
        for x in rd:
            print(x)    
             
        a=input("book the order number ")
        
        sql = "SELECT * FROM product where id =%s"
        va = (a,)
        mycursor.execute(sql,va)
        myresult=mycursor.fetchone()
       
        # ID = myresult[0]
        Product_name = myresult[1]
        size = myresult[2]
        Colour = myresult[3]
            
        sql = "Insert into order(Product_name,size,Colour,Status) Values (%s,%s,%s,%s)"
        var = (Product_name,size,Colour,'Pending')
        mycursor.execute(sql,var)
        mydb.commit()
        
        # print("updated")
        print("Successfully book ")
            
        
        
        
        
         
    
    
    if choice == '2':
        print("view product")
        
        mycursor.execute("select*from order")
        rd = mycursor.fetchall()
        for x in rd:
            print(x)      
        
        print("view a product successfully") 
        
        
    if choice == '3':
        print("deleting booking")     
        
        sql = "DELETE FROM product WHERE product_name = 'hat'"
        mycursor.execute(sql)
        mydb.commit()
        print("Succesfully deleting Product")         
       
    elif choice == '4':
        print("update booking")             
        
        sql = "UPDATE product SET ID = '5' WHERE id = 'pending'"
        mycursor.execute(sql)
        mydb.commit()
        print("booking is pending")
        
        
        
        
     