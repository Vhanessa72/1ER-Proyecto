import tkinter as tk
root = tk.Tk()


def borrar():
    global operando
    operando=''
    pantalla.set('0')

def click(a):
    global operando
    operando += str(a)
    pantalla.set(operando)

def resultado():
    global operando
    try:
        res=str(eval(operando))
    except:
        res='ERROR'
    pantalla.set(res)

root.geometry('415x600')
root.title('CALCULADORA')
root.configure(bg="#8C4966")
tk.Label(root, text='CALCULADORA', bg="#8C4966", fg='black', font=('', 30)).place(x=55, y=30)

operando=''
pantalla= tk.StringVar()

tk.Entry(root, justify='left',width=13,font=('', 32), textvariable=pantalla).place(x=50, y=100)
tk.Button(root, text='Borrar', bd=0,width=10,font=('', 30), command=borrar).place(x=50, y=170)
tk.Button(root, text='1', bd=0,width=3,font=('', 30), command=lambda :click(1)).place(x=50, y=250)
tk.Button(root, text='2', bd=0,width=3,font=('', 30), command=lambda :click(2)).place(x=130, y=250)
tk.Button(root, text='3', bd=0,width=3,font=('', 30), command=lambda :click(3)).place(x=210, y=250)
tk.Button(root, text='4', bd=0,width=3,font=('', 30), command=lambda :click(4)).place(x=50, y=330)
tk.Button(root, text='5', bd=0,width=3,font=('', 30), command=lambda :click(5)).place(x=130, y=330)
tk.Button(root, text='6', bd=0,width=3,font=('', 30), command=lambda :click(6)).place(x=210, y=330)
tk.Button(root, text='7', bd=0,width=3,font=('', 30), command=lambda :click(7)).place(x=50, y=410)
tk.Button(root, text='8', bd=0,width=3,font=('', 30), command=lambda :click(8)).place(x=130, y=410)
tk.Button(root, text='9', bd=0,width=3,font=('', 30), command=lambda :click(9)).place(x=210, y=410)
tk.Button(root, text='+', bd=0,width=3,font=('', 30), command=lambda :click('+')).place(x=290,y=170)
tk.Button(root, text='-', bd=0,width=3,font=('', 30), command=lambda :click('-')).place(x=290, y=250)
tk.Button(root, text='*', bd=0,width=3,font=('', 30), command=lambda :click('*')).place(x=290, y=330)
tk.Button(root, text='/', bd=0,width=3,font=('', 30), command=lambda :click('/')).place(x=290, y=410)
tk.Button(root, text='=',bd=0,width=3,font=('', 30), command=resultado).place(x=290, y=490)
tk.Button(root, text='0',bd=0,width=10,font=('', 30), command=lambda :click(0)).place(x=50, y=490)
root.mainloop()