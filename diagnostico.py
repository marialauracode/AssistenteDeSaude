from tkinter import *












window = Tk()
window.title('Diagnóstico em Python')
window.geometry('300x700')

labelTitulo = Label(window, fg="blue", font=("Arial", 15), text="DIAGNÓSTICO MÉDICO")
labelTitulo.pack(pady=5)


labelNome = Label(window, fg="black", font=("Arial", 11), text="Nome completo do paciente:")
labelNome.pack(anchor="w", padx=5)
entradaNome = Entry(window, width=35)
entradaNome.pack(anchor="w", padx=5, pady=5)
entradaNome.focus()

labelIdade = Label(window, fg="black", font=("Arial", 11), text="Idade do paciente:")
labelIdade.pack(anchor="w", padx=5)
entradaIdade = Entry(window, width=35)
entradaIdade.pack(anchor="w", padx=5, pady=5)

labelSelecionar = Label(window, fg="black", font=("Arial", 11), text="Selecione até três sintomas:")
labelSelecionar.pack(anchor="w", padx=5, pady=5)

sintoma1 = BooleanVar()
sintoma2 = BooleanVar()
sintoma3 = BooleanVar()
sintoma4 = BooleanVar()
sintoma5 = BooleanVar()
sintoma6 = BooleanVar()
sintoma7 = BooleanVar()
sintoma8 = BooleanVar()
sintoma9 = BooleanVar()
sintomaOutros = BooleanVar()


check1 = Checkbutton(window, text="Dor de cabeça", font=("Arial", 11), fg="black", variable=sintoma1)
check1.pack(anchor="w", padx=5)

check2 = Checkbutton(window, text="Dor no corpo", font=("Arial", 11), fg="black", variable=sintoma2)
check2.pack(anchor="w", padx=5)

check3 = Checkbutton(window, text="Dor de garganta", font=("Arial", 11), fg="black", variable=sintoma3)
check3.pack(anchor="w", padx=5)

check4 = Checkbutton(window, text="Dor de dente", font=("Arial", 11), fg="black", variable=sintoma4)
check4.pack(anchor="w", padx=5)

check5 = Checkbutton(window, text="Tosse", font=("Arial", 11), fg="black", variable=sintoma5)
check5.pack(anchor="w", padx=5)

check6 = Checkbutton(window, text="Tontura", font=("Arial", 11), fg="black", variable=sintoma6)
check6.pack(anchor="w", padx=5)

check7 = Checkbutton(window, text="Coriza", font=("Arial", 11),  fg="black", variable=sintoma7)
check7.pack(anchor="w", padx=5)

check8 = Checkbutton(window, text="Enjoo", font=("Arial", 11), fg="black", variable=sintoma8)
check8.pack(anchor="w", padx=5)

check9 = Checkbutton(window, text="Febre", font=("Arial", 11), fg="black", variable=sintoma9)
check9.pack(anchor="w", padx=5)

check10 = Checkbutton(window, text="Outro", font=("Arial", 11), fg="black", variable=sintomaOutros)
check10.pack(anchor="w", padx=5)







window.mainloop()
