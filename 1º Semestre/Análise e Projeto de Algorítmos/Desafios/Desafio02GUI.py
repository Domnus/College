import tkinter as tk
from random import randint 

HEIGHT = 768
WIDTH = 1024

root = tk.Tk()

root.title('Desafio 2')
        
  
def inserir():
    global imagem
    global elem
    global matriz
    global h
    global w  
    h = int(height.get())
    w = int(width.get())
    
    try:
        elem.destroy()
    except Exception:
        pass
    
    imagem = []
    if h <= 20 or w <= 20:
        imagem = [0] * h
        for i in range(h):
            imagem[i] = [0] * w
            cond = 0
            while cond < w:
                x = randint(0, 1)
                if x != 0 and x != 1:
                    print('Digite apenas 1 ou 0!')
                else:
                    imagem[i][cond] = x
                    cond += 1
    
    matriz = ''
    for i in range(len(imagem)):
        elemento = str(imagem[i])
        matriz += elemento
        matriz += '\n'
    elem = tk.Label(upper_frame, text=matriz)
    elem.pack()
    inserir_1['state'] = 'disabled'


def compactar():
    compactacao = []
    for i in range(h):
        p, b = 0, 0
        for j in range(w):
            if(imagem[i][j] == 1):
                p += 1
            if(imagem[i][j] == 0):
                b += 1
            if j == w-1 or imagem[i][j] != imagem[i][j+1]:
                if(p>0):
                    compactacao.append(f'{p}P')
                elif(b>0):
                    compactacao.append(f'{b}B')    
                p, b = 0, 0
        compactacao.append('0')
    compactacao.append('0')
    
    inserir_1['state'] = 'normal'

    T = tk.Text(root, height=1, width=(len(compactacao) *3), bg='blue', fg='white', padx=2, pady=2)
    T.place(relx=0.1, rely=0.7)
    T.insert(tk.END, compactacao)
        

def descompactar(entry):
    global descompactado
    arr = [[]]
    cont = 0
    linhas = 1
    try:
        descompactado.destroy()
    except Exception:
        pass
    for character in entry:
        if character.isdecimal():
            numero = int(character)
        else:
            letra = character
        if numero == 0:
            arr.append([])
            cont += 1
            linhas += 1
            continue
        try:
            if letra == 'B':
                for i in range(numero):
                    arr[cont].append(0)
            elif letra == 'P':
                for i in range(numero):
                    arr[cont].append(1)
            letra = ''
        except Exception:
            pass
        
    for i in range(1):
        arr.pop()
    
    matriz2 = ''
    for i in range(len(arr)):
        elemento = str(arr[i])
        matriz2 += elemento
        matriz2 += '\n'
    descompactado = tk.Label(upper_frame, text=matriz2, bg='white', fg='red')
    descompactado.pack()
        

def botao():
    compactar()
    destroy_label()


def submit():
    tamanho.get()
    tamanho2.get()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='gray')
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

inserir_1 = tk.Button(frame, text="1 – Inserir a imagem (criar a matriz (max. 20x20)", bg='black', fg='white', padx=30, command=inserir)
inserir_1.pack()

height = tk.Entry(frame)
height.pack()

tamanho = tk.Label(frame, text='Altura')
tamanho.place(rely=0.04, relx=0.37)

tamanho2 = tk.Label(frame, text='Largura')
tamanho2.place(rely=0.07, relx=0.36)

width = tk.Entry(frame)
width.pack()

compactar_2 = tk.Button(frame, text='2 – Compactar a imagem', bg='black', fg='white', padx=40.5, command=compactar)
compactar_2.pack()

descompactar_3 = tk.Button(frame, text='3 – Descompactar a imagem', bg='black', fg='white', padx=30, command=lambda: descompactar(entry.get()))
descompactar_3.pack()

entry = tk.Entry(frame)
entry.pack()

sair_4 = tk.Button(frame, text='4 – Sair do programa', bg='black', fg='white', command=quit, padx=53)
sair_4.pack()

upper_frame = tk.Frame(root, bg='#14b6c4', bd=10)
upper_frame.place(relx=0.5, rely=0.3, relheight=0.55, relwidth=0.75, anchor='n')

label = tk.Label(upper_frame, text='Matriz')
label.pack()


root.mainloop()