from tkinter import *

nome_paciente = ""
idade_paciente = ""   # variável global, está fora da função e será modificada dentro da função a seguir

def selecionarNome():
    global nome_paciente
    nome_paciente = entradaNome.get()

def mostrarNome():
    labelResultado.config(text="Nome completo do paciente:", fg="black")
    labelNomePaciente.config(text=nome_paciente, fg="red")   

def Idade():
    global idade_paciente
    idade_paciente = entradaIdade.get()   

def mostrarIdade():

    idade = int(idade_paciente)    

    if (idade > 0 and idade <= 12) :
        labelResultado2.config(text="Idade do paciente: ", fg="black")
        labelIdadePaciente.config(text=f"{idade} (infantil)", fg="red")
    else :
        labelResultado2.config(text="Idade do paciente: ", fg="black")
        labelIdadePaciente.config(text=f"{idade} (adulto)", fg="red")


def executarTudo():
    selecionarNome()
    mostrarNome()
    Idade()
    mostrarIdade()
    verificarOutro()

def verificarOutro(): 
    if varOutro.get():
        labelOutroMensagem.pack(side="left")
    else:
        labelOutroMensagem.pack_forget()



window = Tk()
window.title('Diagnóstico em Python')
window.geometry('300x700')

# Título centralizado
labelTitulo = Label(window, fg="blue", font=("Arial", 15), text="DIAGNÓSTICO MÉDICO")
labelTitulo.pack(pady=5, anchor="center")

# Nome do paciente
labelNome = Label(window, fg="black", font=("Arial", 11), text="Nome completo do paciente:")
labelNome.pack(anchor="w", padx=5)

entradaNome = Entry(window, width=35)
entradaNome.pack(anchor="w", padx=5, pady=5)
entradaNome.focus()

# Idade do paciente
labelIdade = Label(window, fg="black", font=("Arial", 11), text="Idade do paciente:")
labelIdade.pack(anchor="w", padx=5)

entradaIdade = Entry(window, width=35)
entradaIdade.pack(anchor="w", padx=5, pady=5)

# Sintomas
labelSelecionar = Label(window, fg="black", font=("Arial", 11), text="Selecione até três sintomas:")
labelSelecionar.pack(anchor="w", padx=5, pady=5)

# Sintomas com Checkbuttons
check1 = Checkbutton(window, text="Dor de cabeça", font=("Arial", 11), fg="black")
check1.pack(anchor="w", padx=5)

check2 = Checkbutton(window, text="Dor no corpo", font=("Arial", 11), fg="black")
check2.pack(anchor="w", padx=5)

check3 = Checkbutton(window, text="Dor de garganta", font=("Arial", 11), fg="black")
check3.pack(anchor="w", padx=5)

check4 = Checkbutton(window, text="Dor de dente", font=("Arial", 11), fg="black")
check4.pack(anchor="w", padx=5)

check5 = Checkbutton(window, text="Tosse", font=("Arial", 11), fg="black")
check5.pack(anchor="w", padx=5)

check6 = Checkbutton(window, text="Tontura", font=("Arial", 11), fg="black")
check6.pack(anchor="w", padx=5)

check7 = Checkbutton(window, text="Coriza", font=("Arial", 11), fg="black")
check7.pack(anchor="w", padx=5)

check8 = Checkbutton(window, text="Enjoo", font=("Arial", 11), fg="black")
check8.pack(anchor="w", padx=5)

check9 = Checkbutton(window, text="Febre", font=("Arial", 11), fg="black")
check9.pack(anchor="w", padx=5)

varOutro = IntVar()
check10 = Checkbutton(window, text="Outro", font=("Arial", 11), fg="black", variable=varOutro)
check10.pack(anchor="w", padx=5)

labelOutroMensagem = Label(window, text="Você está sentindo outro sintoma?\nEntre em contato com o Dr. Karev\n\nEmail: drkarev@gmail.com\nTelefone: 3013-3053",anchor="w", fg="black", font=("Arial", 10))

# Botão de resultado
botaoResultado = Button(window, text="Resultado", fg="blue", bg="white", font=("Arial", 11), width=10, command=executarTudo)
botaoResultado.pack(pady=5)

frameResultado = Frame(window) # frame maior -> organiza e separa blocos de conteúdos
frameResultado.pack(anchor="w")

frameNome = Frame(frameResultado) # frame (bloco)  para o nome
frameNome.pack(anchor="w")

labelResultado = Label(frameNome, text="", font=("Arial", 10), fg="black")
labelResultado.pack(side="left")

labelNomePaciente = Label(frameNome, text="", font=("Arial", 10), fg="red")
labelNomePaciente.pack(side="left")

frameIdade = Frame(frameResultado) # frame (bloco) para a idade
frameIdade.pack(anchor="w")

labelResultado2 = Label(frameIdade, text="", font=("Arial", 10), fg="black")
labelResultado2.pack(side="left")

labelIdadePaciente = Label(frameIdade, text="", font=("Arial", 10), fg="red")
labelIdadePaciente.pack(side="left")



window.mainloop()
