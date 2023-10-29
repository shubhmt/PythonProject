import psycopg2
from datetime import datetime;
import bcrypt
import hashlib

conn = psycopg2.connect(database = "adep_metadata", 
                        user = "postgres", 
                        host= 'illin4313',
                        password = "postgres",
                        port = 5431)

#MENU CODE
cur = conn.cursor()

class Cab:

    def __init__(self, available=True):
        self.available=available

 

    def book(self):
           if self.available:
            print("cab booked succesfully!")
            self.available=False
           else:
            print("Sorry, the cab driver is not available..")

 

    def release(self):
        self.available=True
        print("Cab released")

    def encrypt_password(self,password1):
          sha256=hashlib.sha256()
          sha256.update(password1.encode('utf-8'))
          return sha256.hexdigest()

 

    def Employee_Login(self):
        input("Enter your username:")
        input("Enter your password:")

 
    def registerEmployee(self,fname,lname,usr,pwd,no):
        cur = conn.cursor()
        sql1='''insert into employee_g2(f_name,l_name) values (%s,%s)'''
        cur.execute(sql1,(fname,lname))
        conn.commit()
        sql2='''insert into sensitive_info_g2(prole,username,pwd,contact_no) values (%s,%s,%s,%s)'''
        cur.execute(sql2,('Employee',usr,pwd,no))
        conn.commit
        date_now=datetime.now().isoformat(sep=" ")
        sql3='''insert into public.log_g2(description, "timestamp") values (%s,%s)'''
        cur.execute(sql3,(f'Employee named {fname} {lname} was registered',date_now))
        cur.close()
        conn.commit()
       

    def NewEmployee(self):
        fname=input("First name:")
        lname=input("Last name:")
        usr=input("Username:")
        pwd=input("pwd:")
        no=input("contact:")
        self.registerEmployee(fname,lname,usr,pwd,no)

 

    def check_credentials(self,usr_name,entered_password):
                    insert_query1 = """
                    Select "pwd" from "sensitive_info_g2" where "username"=%s;
                    """
                    cur.execute(insert_query1, (usr_name,))
                
                    stored_password=cur.fetchone()[0]
                    
                    

                    usr_entered_password=self.encrypt_password(entered_password)

                    
                    print("\n")
                    

                    if usr_entered_password==stored_password:
                         return True
                    
                    else:
                         return False
                    
                    cur.close()
                    conn.commit()
    def Update_driver_details(self):
        #  driver_id=input("enter your driver_id:")
         usrname=input("Enter usrname:")
         update_query=f"update sensitive_info_g2 set pwd=%s where username=%s "
         new_password=input("enter new password:")
         new_password1=self.encrypt_password(new_password)
         cur.execute(update_query,(new_password1,usrname))
         conn.commit()
         cur.close()
         conn.close()
         

    def Unregistered_driver(self):
         delete_driver_id=input("enter your driver id:")
         usr_name=input("Enter your username:")
         delete_query=f"DELETE FROM drivers_g2 where driver_id = {delete_driver_id};"
         delete_query1=f"DELETE FROM sensitive_info_g2 where username = {usr_name};"


         cur.execute(delete_query)
         cur.execute(delete_query1)

         cur.close()
         conn.commit()

                    
   
    def DriverLogin(self,chance):
            if chance<2:
                usr_name=input("Enter your username:")
                entered_password=input("Enter your password:")
               

               
                if self.check_credentials(usr_name,entered_password):
                    print("Congratulations you logged in .......")

                    print("\n 1. Update driver details")
                    print("\n 2. Unregister_driver")

                    choice=input("Enter your choice:")

                    if choice=="1":
                       self.Update_driver_details()
                    elif choice=="2":
                       self.Unregistered_driver()
                    else:
                        exit
                                
                else:
                    print("Password is incorrect!!! Try Again!!")
                    chance=chance+1
                    self.DriverLogin(chance)
            else:
                 print("!!!!!!! Too many wrong attempts !!!!!!!!")




    def registerDriver(self,fname,lname,usr,licence_no,driver_id,password,contact_no):

        cur = conn.cursor()
        sql1='''insert into drivers_g2(driver_id,f_name,l_name,licence_no) values (%s,%s,%s,%s)'''
        cur.execute(sql1,(driver_id,fname,lname,licence_no))
        conn.commit()
        sql2='''insert into sensitive_info_g2(prole,username,pwd,contact_no) values (%s,%s,%s,%s)'''
        cur.execute(sql2,('Driver',usr,password,contact_no))
        conn.commit
        date_now=datetime.now().isoformat(sep=" ")
        sql3='''insert into public.log_g2(description, "timestamp") values (%s,%s)'''
        cur.execute(sql3,(f'Driver named {fname} {lname} was registered',date_now))
        cur.close()
        conn.commit()
       
        
    def NewDriver(self):
            fname = input("Enter your first name:")
            lname=input("Enter your last name:")
            contact_no= input("Enter your Contact_Info:")
            usr=input("Enter username:")
            licence_no = input("Enter your Vehicle Information:")
            driver_id = input("Enter  your Driver_Id:")
            password1 = input("Create your password:")
            password=self.encrypt_password(password1)
            self.registerDriver(fname,lname,usr,licence_no,driver_id,password,contact_no)
            print("\n Congratulation you have registered succesfully!!!!!")
            self.DriverLogin(0)



       

def func():

    cab=Cab()

    while True:
        print("1. Employee Login")
        print("2. Register Employee")
        print("3. Driver Login")
        print("4. Register Driver")
        print("5. Exit")
        choice=input("enter your choice:")
        #print(type(choice))

       

        if choice=="1":
           cab.Employee_Login()
        elif choice=="2":
           cab.NewEmployee()
        elif choice=="3":
           cab.DriverLogin(0)  
        elif choice=="4":
           cab.NewDriver()
        elif choice=="5":
            break
        else:
           print("Invalid choice. Please try again.")

           

 

if __name__ == "__main__":
    func()
    conn.close()

     
