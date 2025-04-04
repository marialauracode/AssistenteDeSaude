from tkinter import *

nome_paciente = ""
idade_paciente = ""
sintomas_selecionados = []  

def selecionarNome():
    global nome_paciente
    nome_paciente = entradaNome.get()

def mostrarNome():
     labelResultado.config(text="Nome completo do paciente:", fg="black",)
     labelNomePaciente.config(text=nome_paciente, fg="red")   

def Idade():
    global idade_paciente
    idade_paciente = entradaIdade.get()   

def mostrarIdade():
    idade = int(idade_paciente)    

    if (idade > 0 and idade <= 12):
        labelResultado2.config(text="Idade do paciente:", fg="black")
        labelIdadePaciente.config(text=f"{idade} (infantil)", fg="red")
    else:
        labelResultado2.config(text="Idade do paciente:", fg="black")
        labelIdadePaciente.config(text=f"{idade} (adulto)", fg="red")

def selecionarSintomas():
    global sintomas_selecionados
    sintomas_selecionados = [sintoma for sintoma, var in check_vars.items() if var.get()]

def mostrarSintomas():
    sintomas_exibidos = [sintoma for sintoma in sintomas_selecionados if sintoma != "Outro"]
    
    if sintomas_exibidos:
        labelResultado3.config(text="Sintomas:", fg="black")
        labelSintomasPaciente.config(text=", ".join(sintomas_exibidos), fg="red", wraplength=285, anchor="w")
        
        labelRecomendacao.config(text="Recomendação médica:", fg="black", wraplength=310)
        labelEspecialista.config(text="Procure um especialista.", fg="red")
    else:
        labelResultado3.config(text="") 
        labelSintomasPaciente.config(text="Nenhum sintoma selecionado", fg="red")
        labelRecomendacao.config(text="")  
        labelEspecialista.config(text="")

def executarTudo():
    selecionarNome()
    mostrarNome()
    Idade()
    mostrarIdade()
    selecionarSintomas()
    mostrarSintomas()
    verificarOutro()

def verificarOutro(): 
    if varOutro.get():
        labelOutroMensagem.pack(pady=2)
    else:
        labelOutroMensagem.pack_forget()

window = Tk()
window.title('Assistente de Saúde Médica')
window.geometry('355x756')

labelTitulo = Label(window, fg="blue", font=("Arial", 15), text="ASSISTENTE DE SAÚDE")
labelTitulo.pack(pady=5, anchor="center")

# Nome do paciente
labelNome = Label(window, fg="black", font=("Arial", 12), text="Nome completo do paciente:")
labelNome.pack(anchor="w", pady=6)

entradaNome = Entry(window, width=37)
entradaNome.pack(anchor="w", padx= 2, pady=3)
entradaNome.focus()

# Idade do paciente
labelIdade = Label(window, fg="black", font=("Arial", 12), text="Idade do paciente:")
labelIdade.pack(anchor="w",  pady=6)

entradaIdade = Entry(window, width=37)
entradaIdade.pack(anchor="w", padx=2 , pady=3)

# Sintomas
labelSelecionar = Label(window, fg="black", font=("Arial", 12), text="Selecione até três sintomas:")
labelSelecionar.pack(anchor="w", padx=5, pady=5)

sintomas = ["Dor de cabeça", "Dor no corpo", "Dor de garganta", "Dor de dente", "Tosse","Tontura", "Coriza", "Enjoo", "Febre"]

check_vars = {sintoma: IntVar() for sintoma in sintomas}

for sintoma, var in check_vars.items():
    Checkbutton(window, text=sintoma, font=("Arial", 11), fg="black", variable=var).pack(anchor="w", padx=5)

varOutro = IntVar()
check10 = Checkbutton(window, text="Outro", font=("Arial", 11), fg="black", variable=varOutro)
check10.pack(anchor="w", padx=5)

labelOutroMensagem = Label(window, text="Você está sentindo outro sintoma?\nEntre em contato com o Dr. Karev\n""Email: drkarev@gmail.com\nTelefone: 3013-3053\n",anchor="w", fg="black", font=("Arial", 10))

# Botão de resultado
botaoResultado = Button(window, text="Resultado", fg= "blue", bg="white", font=("Arial", 11), width=10, command=executarTudo)
botaoResultado.pack(pady=5)

frameResultado = Frame(window)
frameResultado.pack(anchor="w", pady=6)

frameNome = Frame(frameResultado)
frameNome.pack(anchor="w")

labelResultado = Label(frameNome, text="", font=("Arial", 11), fg="black")
labelResultado.pack(side="left", pady=5)

labelNomePaciente = Label(frameNome, text="", font=("Arial", 11), fg="red", wraplength=180)
labelNomePaciente.pack(side="left")

frameIdade = Frame(frameResultado)
frameIdade.pack(anchor="w")

labelResultado2 = Label(frameIdade, text="", font=("Arial", 11), fg="black")
labelResultado2.pack(side="left", pady=5)

labelIdadePaciente = Label(frameIdade, text="", font=("Arial", 11), fg="red")
labelIdadePaciente.pack(side="left")

frameSintomas = Frame(frameResultado)
frameSintomas.pack(anchor="w")

frameRecomendacao = Frame(frameResultado)
frameRecomendacao.pack(anchor="w")

labelRecomendacao = Label(frameRecomendacao, text="", font=("Arial", 11), fg="red")
labelRecomendacao.pack(anchor="w", side="left", pady=5)

labelEspecialista = Label(frameRecomendacao, text="", font=("Arial", 11), fg="red")
labelEspecialista.pack(pady=5)

labelResultado3 = Label(frameSintomas, text="", font=("Arial", 11), fg="black")
labelResultado3.pack(anchor="w", side="left", pady=5)

labelSintomasPaciente = Label(frameSintomas, text="", font=("Arial", 11), fg="red")
labelSintomasPaciente.pack(side="left", anchor="w")

window.mainloop()
