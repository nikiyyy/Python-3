# изготвено от Николай Иванов №17621301
from tkinter import * # импортирам библиотеката tkinter за създаване на графичен интерфайс
from tkinter.filedialog import askopenfilename
import balkp as BA #импортирам бакенда на програмата
def searchfile(): #функцията seravhfile си използва за търсене на файлове когато бутон 1 е актевиран
    window.fileName = askopenfilename(filetypes = ( ("textfile" ,".txt"), ("All files","*") ) )
    e1.insert(0, str(window.fileName)) # записвам адреса на файла в текстовата кутия
    l1['text']="File selected" #променям индекатора за наличност на файл
    l1['fg']="Green"

def start(): #тази функция стартира бакенда на програмата
    if str(window.fileName)!= "": # проверка дали има избран файл
        BA.fun(window.fileName) #викане на бакенда
    else:
        l1['text']="Chose file" 
    
window=Tk()#създавам tk обект за графичен интерфайс
window.title(" Least cost method problem solver")
window.resizable(width=False, height=False) 

#бутон за избране на файл който повиква searchfile()
b1=Button(window,text="Chose file", width=16,command=searchfile)
b1.grid(row=1, column=1)

#бутон за стартиране бакенда на програмата start()
b2=Button(window,text="Generate solution", width=16,command=start)
b2.grid(row=2, column=1)

textVar="Please select a file" #индикатор за валидност
l1=Label(text = textVar , fg='Red' ,bd=5) 
l1.grid(row=2, column=2)

e1=Entry(window,width=40)# entry за въвеждане на дайл
e1.grid(row=1, column=2)
window.mainloop()