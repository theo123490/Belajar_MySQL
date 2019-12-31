import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='pass12345',
    database='belajar', 
    # port = '3306'
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE item_list(id INT(6) UNSIGNED AUTO_INCREMENT KEY, item_name VARCHAR(60) NOT NULL, item_desc VARCHAR(300) NOT NULL,item_type VARCHAR(30) NOT NULL, reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)")
# last_id = mycursor.fetchone()[0]
# mydb.commit()

# mycursor = mydb.cursor()

asst_name_list = ["Ais"]
                
pursuing_degree_list = ['S1']

batch_list = ['2016']

speciality_list = ["L"]

for i in range(len(asst_name_list)):
    sqlform = "INSERT INTO lab_assistant (asst_name, pursuing_degree, batch, specialty) VALUES (%s,%s,%s,%s)"
    
    asst_name=asst_name_list[i].replace(' ','%123%')
    pursuing_degree = pursuing_degree_list[i].replace(' ','%123%')
    batch = batch_list[i].replace(' ','%123%')
    speciality = speciality_list[i].replace(' ','%123%')
    variables =(asst_name,pursuing_degree,batch,speciality)

    print('updating data with item {} data: {}'.format(asst_name,variables))

    # print(sqlform.format(*variables))
    mycursor.execute(sqlform,variables)
    mydb.commit()
    print('Done Updating')
