from tkinter import *


jn = Tk()
jn.geometry("220x300")
jn.maxsize(height=220, width=215)
jn.minsize(height=260, width=215)
jn.configure(bg="powder blue")

def igual():
    segundo_numero = tela.get()
    tela.delete(0, END)
    if matematica == "soma":
        tela.insert(0, p_numero + float(segundo_numero))
    if matematica == "subtração":
        tela.insert(0, p_numero - float(segundo_numero))
    if matematica == "multiplicação":
        tela.insert(0, p_numero * float(segundo_numero))
    if matematica == "divisão":
        tela.insert(0, p_numero / float(segundo_numero))

def virgula():
    tela.insert(END, ",")

def multiplicação():
    prim_numero = tela.get()
    global p_numero
    global matematica
    matematica = "multiplicação"
    p_numero = float(prim_numero)
    tela.delete(0, END)

def divisao():
    prim_numero = tela.get()
    global p_numero
    global matematica
    matematica = "divisao"
    p_numero = float(prim_numero)
    tela.delete(0, END)


def subtração():
    prim_numero = tela.get()
    global p_numero
    global matematica
    matematica = "subtração"
    p_numero = float(prim_numero)
    tela.delete(0, END)

def soma():
    prim_numero = tela.get()
    global p_numero
    global matematica
    matematica = "soma"
    p_numero = float(prim_numero)
    tela.delete(0, END)


def deletar():
    tela.delete(0,END)


def click_botao(numero):
    atual = tela.get()
    tela.delete(0, END)
    tela.insert(END, str(atual)+ str(numero))

tela = Entry(jn, width = 30, border=5)
tela.place(x = 10, y=25) 

botao1 = Button(jn, text = "7", width=5, command=lambda: click_botao(7))
botao1.place(x= 10, y = 100)

botao2 = Button(jn, text="8", width=5, command=lambda: click_botao(8))
botao2.place(x = 60, y =100)

botao3= Button(jn, text = "9", width =5, command=lambda: click_botao(9))
botao3.place(x = 110, y = 100)

botao4 = Button(jn, text = "4", width=5, command=lambda: click_botao(4))
botao4.place(x=10, y = 130 )

botao5 = Button(jn, text = "5", width=5, command=lambda: click_botao(5))
botao5.place(x = 60, y=130)

botao6 = Button(jn, text="6", width=5, command=lambda: click_botao(6))
botao6.place(x = 110, y = 130)

botao7 = Button(jn, text="1", width=5, command=lambda: click_botao(1))
botao7.place(x = 10, y = 160)

botao8 = Button(jn, text="2", width=5, command=lambda: click_botao(2))
botao8.place(x = 60, y =160)

botao9 = Button(jn, text="3", width=5, command=lambda: click_botao(3))
botao9.place(x = 110, y = 160)

botao0 = Button(jn,text="0", width=12, command=lambda: click_botao(0))
botao0.place(x = 10, y = 190)

botaoVIR = Button(jn, text=",", width=5, command=virgula)
botaoVIR.place(x = 110, y = 190)

botaomais = Button(jn, text="+", width=5, command=soma)
botaomais.place(x = 160, y = 190)

botaominus = Button(jn, text="-", width=5, command=subtração)
botaominus.place(x = 160, y =160)

botaox = Button(jn, text="x", width=5, command=multiplicação)
botaox.place(x = 160,y = 130)

botaodiv = Button(jn, text="/", width=5, command=divisao)
botaodiv.place(x = 160, y = 100)

botaoigual = Button(jn, text="=", width=19, command=igual)
botaoigual.place(x = 10 , y = 220)

botaoapag = Button(jn, text=" << ", width= 5, command=deletar)
botaoapag.place(x = 160, y = 220)








jn.mainloop()