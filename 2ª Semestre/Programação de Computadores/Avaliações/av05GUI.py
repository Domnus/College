import tkinter as tk
from random import randint

HEIGHT = 768
WIDTH = 1024

root = tk.Tk()

root.title('Cores em RGB')

cores = {}

def inserir():
    list = upper_frame.pack_slaves()
    for l in list:
        l.destroy()

    _cor = cor.get()
    _codigo = codigo.get()

    if _cor in cores.keys():
        elem = tk.Label(upper_frame, text="Cor já cadastrada!")
        elem.pack()
    else:
        cores[_cor] = _codigo


def consulta():
    nomeCor = corConsulta.get()
    for x, y in cores.items():
        if nomeCor == x:
            return ["True", y]
    return ["False"]


def _consulta():
    v = consulta()

    list = upper_frame.pack_slaves()
    for l in list:
        l.destroy()

    if v[0] == "True":
        elem = tk.Label(upper_frame, text=f"Código da cor: {v[1]}")
        elem.pack()
    else:
        elem = tk.Label(upper_frame, text="Cor inválida!")
        elem.pack()


def listagem():
    list = upper_frame.pack_slaves()
    for l in list:
        l.destroy()

    if cores == {}:
        elem = tk.Label(upper_frame, text="Lista vazia!")
        elem.pack()
    else:
        for x, y in cores.items():
            elem = tk.Label(upper_frame, text=f"Cor: {x} | Código: {y}")
            elem.pack()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='gray')
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

inserirB = tk.Button(frame, text='Inserir', command=inserir)
inserirB.pack()

tamanho = tk.Label(frame, text='Cor')
tamanho.place(rely=0.04, relx=0.37)

cor = tk.Entry(frame)
cor.pack()

tamanho2 = tk.Label(frame, text='Código')
tamanho2.place(rely=0.065, relx=0.36)

codigo = tk.Entry(frame)
codigo.pack()

consultaB = tk.Button(frame, text='Consulta', command=_consulta)
consultaB.pack()

corConsulta = tk.Entry(frame)
corConsulta.pack()

listagemB = tk.Button(frame, text='Listagem', command=listagem)
listagemB.pack()

sair = tk.Button(frame, text='Sair do programa', command=quit)
sair.pack()

upper_frame = tk.Frame(root, bg='#14b6c4', bd=10)
upper_frame.place(relx=0.5, rely=0.3, relheight=0.55, relwidth=0.75, anchor='n')


root.mainloop()

