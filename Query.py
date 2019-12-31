import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='pass12345',
    database='belajar'
)

asst_name_input = ("Theodre",)
mycursor = mydb.cursor()
sqlform = """
SELECT REPLACE(item_name,'%123%',' ')
FROM item_list
	inner join type_list on type_code = item_list.item_type
	inner join lab_assistant on specialty = item_list.item_type
WHERE lab_assistant.asst_name = %s
"""
# print(sqlform)
mycursor.execute(sqlform,asst_name_input)
if (mycursor.fetchone()!=None):
    for i in mycursor:
        print(i)
else:
    print("NO DATA AVAILABLE")