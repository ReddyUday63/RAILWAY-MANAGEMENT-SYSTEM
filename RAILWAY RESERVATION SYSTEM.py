import mysql.connector
import numpy as np
import time
k=[]

conn=mysql.connector.connect(host="localhost",user="root",password="1234")
cursor=conn.cursor()
conn.autocommit=True

s1="create database if not exists railway"
cursor.execute(s1)
s1="use railway"
cursor.execute(s1)
s1="create table if not exists railway(name varchar(100),phno varchar(15),age int(4),gender varchar(50),from_s varchar(100),to_d varchar(100),Date_of_Journey varchar(20))"
cursor.execute(s1)

s="create table if not exists rail_accounts(Name varchar(100),UserNAME varchar(100),Password varchar(100),Phone_Number varchar(15),gender varchar(50),dob varchar(50),age varchar(4))"
cursor.execute(s)

def ticket_booking():
    time.sleep(0.3)
    print("REDIRECTING TO THE TICKET-BOOKING PAGE".center(100,"-"))
    time.sleep(1)
    name=input("ENTER YOUR NAME:")
    phn=input("Enter Your phone number:")
    age=int(input("enter your age:"))
    fr=input("Enter the starting point of your journey:")
    to=input("Enter the destination point of your journey:")
    d=input("enter day(1-30):")
    m=input("enter month(1-12):")
    y=input("Enter year:")
    dmy=d+":"+m+":"+y
    print("M:Male","F:Female","N:Not Preferred to say")
    gender=input("Enter Your Gender:")
    gen=gender.upper()
    v={"M":"Male","F":"Female","N":"Not Preferred to say"}
    g=v[gen]
    bq="insert into railway values('{}','{}','{}','{}','{}','{}','{}')".format(name,phn,age,g,fr,to,dmy) #booking query
    cursor.execute(bq)
    print("TICKET BOOKED SUCCESFULLY...")
    main()

def ticket_checking():
    global cursor  # Assuming 'cursor' is a global variable
    # Get phone number from user input or any other source
    time.sleep(0.3)
    print("REDIRECTING TO THE TICKET-BOOKING PAGE".center(100,"-"))
    time.sleep(1)
    phn = int(input("ENTER PHONE NUMBER THAT YOU USED FOR BOOKING TICKETS TO SHOW:"))

    # Execute the query
    query = "SELECT * FROM railway WHERE phno = {}".format(phn)
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Check if any rows are returned
    if not rows:
        print("No records found for the given phone number.")
    else:
        # Print the header
        print("HERE ARE THE TICKETS THAT BOOKED WITH YOUR PHONE NUMBER".center(100,"-"))
        print("{:<20} {:<15} {:<5} {:<8} {:<10} {:<10} {:<15}".format(
            "Name", "Phone", "Age", "Gender", "From", "To", "Date of Journey"
        ))
        print("-" * 90)

        # Print the rows in a tabular format
        for row in rows:
            print("{:<20} {:<15} {:<5} {:<8} {:<10} {:<10} {:<15}".format(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6]
            ))
    main()
def ticket_cancelling():
    time.sleep(0.3)
    print("REDIRECTING TO THE TICKET-CANCELLATION PAGE".center(100,"-"))
    time.sleep(1)
    phn=input("Enter Your Phone Number:") #because phone number is unique for everyone
    if cursor.execute(f"SELECT * FROM railway WHERE phno ={phn}"):
        inp=input(f"DO YOU WANT TO CANCEL ALL TICKETS THAT ARE BOOKED WITH {phn}?(Yes/No):")
        if inp.lower()=="yes":
            chq="delete from railway where phno={}".format(phn)
            cursor.execute(chq)
            print("CANCELLING TICKETS".center(100,"-"))
            time.sleep(0.8)
            print(f'TICKETS BOOKED WITH {phn} HAS BEEN CANCELLED SUCCESFULLY'.center(100,"-"))
    else:
        print(f"SORRY...TICKETS are UNAVAILABLE to cancel with this {phn}".center(100,"-"))
        time.sleep(1)
    

# MAIN FUNCTION

def main():
    while True:
        print("1.TICKET BOOKING")
        print("2.TICKET CHECKING")
        print("3.TICKET CANCELLING") 
        print("4. LOG OUT")
        ch=int(input('ENTER YOUR CHOICE:'))
        if ch==1:
            ticket_booking()
        elif ch==2:
            ticket_checking()
        elif ch==3:
            ticket_cancelling()
        elif ch==4:
            print("THANK YOU FOR USING RAILWAY RESERVATION SYSTEM".center(100,"-"))
            time.sleep(1)
            kmain()
        else:
            print("SORRY!!!!!You Entered Wrong Choice".center(100,"-"))
            main()
            break

def sign_up():
    time.sleep(0.5)
    print("REDIRECTING TO THE SIGN-UP PAGE".center(100,"-"))
    time.sleep(1.5)
    print("WELCOME TO SIGN UP PAGE".center(100,"-"))
    time.sleep(1)
    first_name=input("First Name:")
    last_name=input("Last_name:")
    name=first_name+" "+last_name
    username=input("Enter USERNAME:")
    if username.lower() not in k:
        k.append(username.lower())
    else:
        print("USERNAME ALREADY TAKEN BY OTHERS:")
        kmain()
    password=input("Enter Password:")
    re_enter=input("ReEnter Password:")
    phn=input("Enter Your Mobile Number:")
    print("M:Male","F:Female","N:Not Preferred to say")
    v={"M":"Male","F":"Female","N":"Not Preferred to say"}
    gender=input("Enter Your Gender:")
    gen=gender.upper()
    g=v[gen]
    print("Enter Your Date of Birth")
    y=input("Year:")
    m=input("Month:")
    d=input("Date:")
    dmy=d+":"+m+":"+y
    age=input("Enter Your age:")
    if(password==re_enter):   #rail accounts query(raq)
        raq="insert into rail_accounts values('{}','{}','{}','{}','{}','{}','{}')".format(name,username,password,phn,g,dmy,age)
        cursor.execute(raq)
        time.sleep(0.5)
        print("SIGN UP DONE SUCCESFULLY".center(100,"-"))
        main()
    else:
        print("SORRY!!!!!!Password doesn't matched".center(100,"-"))

def sign_in():
    time.sleep(0.5)
    print("REDIRECTING TO THE SIGN-IN PAGE".center(100,"-"))
    time.sleep(1.5)
    print()
    print("WELCOME TO SIGN IN PAGE".center(100,"-"))
    time.sleep(1)
    username = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
    
    try:
        # Use placeholders in the SQL query to prevent SQL injection
        siq = 'SELECT username FROM rail_accounts WHERE username = %s AND password = %s'
        cursor.execute(siq, (username, password))
        data = cursor.fetchone()

        if data and data[0].lower() == username.lower():
            time.sleep(0.5)
            print("SIGNED IN SUCCESSFULLY".center(100,"-"))
            main()
        else:
            print("ACCOUNT NOT FOUND")
    except Exception as e:
        print("Error during sign-in:", e)

def exit():
    print("YOU ARE EXITING RAILWAY MANAGEMENT SYSTEM".center(100,"-"))
    print()
    time.sleep(1.5)
    print("DEVELOPED BY UDAY".center(100,"-"))
    print()
    time.sleep(2)
    print('THANK YOU'.center(100,"-"))
def kmain():
    while(True):
        time.sleep(1)
        print("🙏🏽🙏🏽🙏🏽🙏🏽🙏🏽🙏🏽🙏🏽🙏🏽🙏🏽🙏🏽🙏🏽🙏🏽🙏🏽🙏🏽".center(93,"-"))
        print()
        time.sleep(1)
        print('WELCOME TO RAILWAY MANAGEMENT SYSTEM'.center(100,"-"))
        print()
        time.sleep(1)
        print('1.SIGN UP'.center(50," "))
        print('2.SIGN IN'.center(50," "))
        print("3.EXIT".center(45," "))
        ch=int(input('Enter Your Choice:'))
        if(ch==1):
            sign_up()
        elif(ch==2):
            sign_in()
        elif(ch==3):
            exit()
            break
kmain()