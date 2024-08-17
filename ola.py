import tkinter as tk

#Confi Pantalla
ventana = tk.Tk()
ventana.geometry("300x400")
ventana.title("Calculadoron")

    #Commands
def Resolver():
    op = entrada.get()
    res = eval(op)
    res1 =str(res)
    entrada.delete(0,tk.END)
    entrada.insert(tk.END,res1)
def btn_ten(numero):
    entrada.insert(tk.END,numero)
def clean():
    entrada.delete(0,tk.END)

    #Widgets
entrada = tk.Entry(font=("Arial",28), width=20)
entrada.grid(row=0,column=0,columnspan= 15)
btn_txt = "Resolver"
btn = tk.Button(text=btn_txt, font=("Arial",16), command=Resolver)
btn.grid
    #botones
botones =[
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","+"],
    ["0","AC","-","="]
    ]
for i in range(4):
    for j in range(4):
        texto = botones[i][j]
        if texto == "=":
            boton = tk.Button(text=texto, width=6, height=3, font=("Arial",10),command=Resolver)
        elif texto == "AC":
            boton = tk.Button(text=texto, width=6, height=3, font=("Arial",10),command=clean)
        
        else:

            boton = tk.Button(text=texto, width=6, height=3, font=("Arial",10),command= lambda numero = texto: btn_ten(numero))
        boton.grid(row=i+1, column=j, pady= 3)
        
ventana.mainloop()
