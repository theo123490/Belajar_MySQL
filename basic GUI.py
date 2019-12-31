import tkinter as tk 

import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='pass12345',
    database='belajar'
)

class GUI():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("CARI TANGGUNG JAWAB")
        
        self.lbl_nama = tk.Label(self.window, text="Nama : ")
        self.lbl_nama.grid(column=0, row=0, )

        self.input_nama = tk.Entry(self.window, width=30)
        self.input_nama.grid(column=1, row=0)

        self.lbl_output = tk.Label(self.window, text="Tanggung Jawab : ")
        self.lbl_output.grid(column=0,row=1)

        self.output_text = tk.Text(self.window, width=30, height=20)
        self.output_text.grid(column=1, row=1)

        self.find_bttn = tk.Button(self.window, text="Find", command=self.find_instruments)
        self.find_bttn.grid(column=2,row=0)


        self.window.mainloop()

    
    def find_instruments(self):
        self.output_text.delete(1.0,tk.END)
        asst_name_input = (self.input_nama.get(),)
        mycursor = mydb.cursor()

        sqlform = """
        SELECT REPLACE(item_name,'%123%',' ')
        FROM item_list
            inner join type_list on type_code = item_list.item_type
            inner join lab_assistant on specialty = item_list.item_type
        WHERE lab_assistant.asst_name = %s
        """
        mycursor.execute(sqlform,asst_name_input)

        output_string='='*5+'\n'

        if (mycursor.fetchone()!=None):
            self.output_text.insert(tk.END,"tanggung jawab : \n")

            for i in mycursor:
                output_string = output_string+str(i[0])+"\n"
                print(i)
        else:
            output_string = output_string+"NO DATA AVAILABLE \n"

        output_string=output_string+'='*5+'\n'

        self.output_text.insert(tk.END,output_string)



GUI()