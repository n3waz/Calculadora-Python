from tkinter import *

obj = Tk()
obj.title("Calculadora")
obj.geometry("472x500")
obj.resizable(0,0)
obj.configure(background="dark gray")

resultado = Label(obj, text="0", bg= "dark gray")
resultado.grid(row=0, column=0, pady=(150, 30), columnspan=5, sticky="nsew")
resultado.config(font=('verdena', 30, 'bold'))

# Primeira linha
button7 = Button(obj, text="7", bg='#EBF7F5', fg='black', width=9, height=2)
button7.grid(row=1, column=0)
button7.config(font=('verdena', 14, 'bold'))

button8 = Button(obj, text="8", bg='#EBF7F5', fg='black', width=9, height=2)
button8.grid(row=1, column=1)
button8.config(font=('verdena', 14, 'bold'))

button9 = Button(obj, text="9", bg='#EBF7F5', fg='black', width=9, height=2)
button9.grid(row=1, column=2)
button9.config(font=('verdena', 14, 'bold'))

soma = Button(obj, text="+", bg='#EBF7F5', fg='black', width=9, height=2)
soma.grid(row=1, column=3)
soma.config(font=('verdena', 14, 'bold'))

# Segunda linha
button4 = Button(obj, text="4", bg='#EBF7F5', fg='black', width=9, height=2)
button4.grid(row=2, column=0)
button4.config(font=('verdena', 14, 'bold'))

button5 = Button(obj, text="5", bg='#EBF7F5', fg='black', width=9, height=2)
button5.grid(row=2, column=1)
button5.config(font=('verdena', 14, 'bold'))

button6 = Button(obj, text="6", bg='#EBF7F5', fg='black', width=9, height=2)
button6.grid(row=2, column=2)
button6.config(font=('verdena', 14, 'bold'))

subtracao = Button(obj, text="-", bg='#EBF7F5', fg='black', width=9, height=2)
subtracao.grid(row=2, column=3)
subtracao.config(font=('verdena', 14, 'bold'))

# Terceira linha
button1 = Button(obj, text="1", bg='#EBF7F5', fg='black', width=9, height=2)
button1.grid(row=3, column=0)
button1.config(font=('verdena', 14, 'bold'))

button2 = Button(obj, text="2", bg='#EBF7F5', fg='black', width=9, height=2)
button2.grid(row=3, column=1)
button2.config(font=('verdena', 14, 'bold'))

button3 = Button(obj, text="3", bg='#EBF7F5', fg='black', width=9, height=2)
button3.grid(row=3, column=2)
button3.config(font=('verdena', 14, 'bold'))

multiplicacao = Button(obj, text="x", bg='#EBF7F5', fg='black', width=9, height=2)
multiplicacao.grid(row=3, column=3)
multiplicacao.config(font=('verdena', 14, 'bold'))

# Quarta linha
button0 = Button(obj, text="0", bg='#EBF7F5', fg='black', width=9, height=2)
button0.grid(row=4, column=0)
button0.config(font=('verdena', 14, 'bold'))

limpar = Button(obj, text="APAGAR", bg='#EBF7F5', fg='black', width=9, height=2)
limpar.grid(row=4, column=1)
limpar.config(font=('verdena', 14, 'bold'))

divisao = Button(obj, text="/", bg='#EBF7F5', fg='black', width=9, height=2)
divisao.grid(row=4, column=2)
divisao.config(font=('verdena', 14, 'bold'))




obj.mainloop()