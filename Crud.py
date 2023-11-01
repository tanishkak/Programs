import mysql.connector 
connect=mysql.connector.connect(user = 'root',host = 'localhost',database="college",passwd='9876')
cursor=connect.cursor()
print(connect,"connected")

def create_db():
    cursor.execute("create table stud_info(id int,name varchar(90),phone_number bigint,city varchar(90))")
    print("table created")

def insert_values():
    id=int(input("Enter the id of student:"))
    name=str(input("Enter the name of student:"))
    phone_number=int(input("Enter the contact no. of student:"))
    city=str(input("Enter the city name of student:"))
    cursor.execute("insert into stud_info values(%s,%s,%s,%s)",(id,name,phone_number,city))
    connect.commit()
    print("record inserted")
    cursor.execute("select * from stud_info")
    print(cursor.fetchall())
    

def update_values():
    id_no=int(input("enter the id you want to update : "))
    n=int(input("what do you want to update: \n 1. Name \n 2. Phone number \n 3. City\n Enter your option:"))
    if n==1:
        uname=str(input("Enter the name of student:"))
        cursor.execute("update stud_info set name=%s where id=%s",(uname,id_no))
        connect.commit()
    if n==2:
        uphone_number=int(input("Enter the contact no. of student:"))
        cursor.execute("update stud_info set phone_number=%s where id=%s",(uphone_number,id_no))
        connect.commit()
    if n==3:
        ucity=str(input("Enter the city name of student:"))
        cursor.execute("update stud_info set city=%s where id=%s",(ucity,id_no))
        connect.commit()
    print("record updated")

def delete_record():
    s=(input("Enter the ID you want to delete : "))
    t=[s]
    cursor.execute("delete from stud_info where id=%s",(t))
    connect.commit()
    print("record deleted")



option=int(input("What operation do you want to perform:\n1.Create\n2.Insert\n3.Update\n4.Delete\nFor exit enter 0 \nEnter your choice: "))

while(option!=0):
    if option==1:
        create_db()
        break
    if option==2:
        insert_values()
        break
    if option==3:
        update_values()
        break
    if option==4:
        delete_record()
        break
    


