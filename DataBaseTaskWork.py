import sqlite3

print("Operatin Code:- c = Creat, a = add data, r = read data, u =update, d = delete")
ope=input("Enter Operation:- ")
file_name= input("\nEnter File Name to connect:- ")
conn=sqlite3.connect(file_name)

def creat():
    conn.execute('''CREATE TABLE LIST
    (ID INT PRIMARY KEY NOT NULL, 
    PRODUCT TEXT NOT NULL,
    PRICE REAL NOT NULL)''')
def insert_code():
    id_num = input("Enter Id number:- ")
    product_name = input("Enter Product Name:- ")
    prodct_rate = input("Enter Product Rate:-")
    sql = ("""INSERT INTO LIST (ID,PRODUCT,PRICE) \
                             VALUES('{}','{}','{}')""".format(id_num, product_name, prodct_rate))
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

def add_data():
    while True:
        print("Code:- a= add data,O = exit")
        perfom=input("Enter Code:- ")
        if perfom=="a":
            insert_code()
        elif perfom=="0":
            break
        else:
            print("invalid code\n")
def read_data():
    print("Id, Product , Price")
    cur_sor="SELECT * FROM LIST"
    for row in conn.execute(cur_sor):
        print(row)
    print("Read all Data\n")

def update():
    print("Id, Product , Price")
    id = input("Enter Id no.: ")
    product = input("Enter Title Head: ")
    data = input("Enter data: ")
    conn.execute(f"UPDATE LIST set {product} = {data} where id = {id}")
    print("Total changes : ", conn.total_changes)
    conn.commit()
    print("Data Updated")
    read_data()

def delete_data():
    id_num = input("Enter Id no.: ")
    conn.execute(f"DELETE from LIST where id = {id_num}")
    print("Total changes : ", conn.total_changes)
    conn.commit()
    # read_data()

if ope == "c":
    creat()
    print("Table Created")
elif ope == "a":
    read_data()
    add_data()
    print("Data added in Table")
elif ope == "r":
    read_data()
elif ope == "u":
    read_data()
    update()
elif ope == "d":
    # read_data()
    delete_data()
else:
    print("Invalid Code")

conn.close()



