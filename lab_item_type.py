import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='pass12345',
    database='belajar'
    )

mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE item_list(id INT(6) UNSIGNED AUTO_INCREMENT KEY, item_name VARCHAR(60) NOT NULL, item_desc VARCHAR(300) NOT NULL,item_type VARCHAR(30) NOT NULL, reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)")
# last_id = mycursor.fetchone()[0]
# mydb.commit()

# mycursor = mydb.cursor()

type_code_list = ['FO','L','IM','S']
                
type_desc_list = ['Fiber Optic','Laser','Image Processing','Spectroscopy']

for i in range(len(type_code_list)):
    sqlform = "INSERT INTO type_list (type_code, type_desc) VALUES (%s,%s)"
    
    type_code=type_code_list[i].replace(' ','%123%')
    type_desc = type_desc_list[i].replace(' ','%123%')

    variables =(type_code,type_desc)

    print('updating data with item {} data: {} '.format(type_code,variables))
    # print(sqlform.format(*variables))
    mycursor.execute(sqlform,variables)
    mydb.commit()
    print('Done Updating')
