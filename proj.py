import psycopg2;
from datetime import datetime;

conn = psycopg2.connect(database = "adep_metadata", 
                        user = "postgres", 
                        host= 'illin4313',
                        password = "postgres",
                        port = 5431)

#MENU CODE

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

 

    def DriverLogin(self):
        input("Enter your username:")
        input("Enter your password:")

 

       

    def NewDriver(self):
        input("Enter your name:")
        input("Enter your age:")
        input("Enter your Gender:")
        input("Enter your emailid:")
        input("Enter your CarName:")


       

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
           cab.DriverLogin()  
        elif choice=="4":
           cab.NewDriver()
        elif choice=="5":
            break
        else:
           print("Invalid choice. Please try again.")

           

 

if __name__ == "__main__":
    func()
    conn.close()

     