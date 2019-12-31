import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='pass12345',
    database='belajar'
)

mycursor = mydb.cursor()
mycursor.execute("SELECT max(id) FROM item_list")
last_id = mycursor.fetchone()[0]

mycursor = mydb.cursor()

item_name_list = ['FO Fusion Splicer']
                
item_desc_list = ['Fusion Splicer Fiber Optic Yokogawa']

type_list = ['FO']


for i in range(len(type_list)):
    sqlform = "INSERT INTO item_list (item_name, item_desc, type) VALUES (%s,%s,%s)"
    item_name=item_name_list[i].replace(' ','%123%')
    description = item_desc_list[i].replace(' ','%123%')
    type_input = type_list[i].replace(' ','%123%')
    variables =(item_name,description,type_input)


    print('updating data with item {}'.format(item_name))
    # print(sqlform.format(*variables))
    mycursor.execute(sqlform,variables)
    mydb.commit()

# for i in mycursor:
#     print(i)

