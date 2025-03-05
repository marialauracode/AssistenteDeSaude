from tkinter import *

nome_paciente = ""  # variável global, está fora da função e será modificada dentro da função a seguir

def selecionarNome():
    global nome_paciente
    nome_paciente = entradaNome.get()

def mostrarNome():
    labelResultado.config(text="Nome completo do paciente:", fg="black")
    labelNomePaciente.config(text=nome_paciente, fg="red")

def executarTudo():
    selecionarNome()
    mostrarNome()

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

check10 = Checkbutton(window, text="Outro", font=("Arial", 11), fg="black")
check10.pack(anchor="w", padx=5)

# Botão de resultado
botaoResultado = Button(window, text="Resultado", fg="blue", bg="white", font=("Arial", 11), width=10, command=executarTudo)
botaoResultado.pack(pady=5)

frameResultado = Frame(window)
frameResultado.pack(anchor="w")
# Label para o resultado
labelResultado = Label(frameResultado, font=("Arial", 10), anchor="w", wraplength=250)
labelResultado.pack(side="left", padx=2)

# Label para o nome do paciente
labelNomePaciente = Label(frameResultado, text="", font=("Arial", 10), anchor="w", wraplength=250)
labelNomePaciente.pack(side="left", padx=2)

window.mainloop()
