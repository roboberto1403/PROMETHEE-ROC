from promethee import calcular_fluxos, ordenar_alternativas
import tkinter as tk
from tkinter import ttk

def promethee_roc(alternativas, criterios, dados):
    # ROC
    criterios_com_pesos = []
    somatorio = 0
    for i in range(len(criterios)-1, -1, -1):
        criterios_com_pesos.append((f"{criterios[i]}", 1/len(criterios) * (somatorio + 1/(i+1))))
        somatorio += 1/(i+1)
    criterios_com_pesos.reverse()
    print("Pesos calculados usando ROC:")
    print(criterios_com_pesos)

    fluxos_totais, fluxos_positivos, fluxos_negativos, indices = calcular_fluxos(alternativas, criterios_com_pesos, dados)
    alternativas_ordenadas = ordenar_alternativas(alternativas, fluxos_totais)
    print(fluxos_positivos)
    print(fluxos_negativos)
    print(indices)

    print("\nRanking das Alternativas:")
    for i, (alternativa, fluxo) in enumerate(alternativas_ordenadas, 1):
        print(f"{i}. {alternativa}: {fluxo}")

def enviar_criterios_alternativas():
    todos_criterios = entry_criterios.get()
    criterios = todos_criterios.split(", ")
    todas_alternativas = entry_alternativas.get()
    alternativas = todas_alternativas.split(", ")
    print(f"Criterios: {criterios}")
    print(f"Alternativas: {alternativas}")

    atualizar_tela_inserir_valores(alternativas, criterios)

def atualizar_tela_inserir_valores(alternativas, criterios):
    # remove componentes
    label_criterios.grid_forget()
    entry_criterios.grid_forget()
    label_alternativas.grid_forget()
    entry_alternativas.grid_forget()

    for widget in entrada_frames:
        widget.destroy()
    entrada_frames.clear()

    line_count = 0
    for i in range(len(alternativas)):
        label_alternativa = ttk.Label(frame, text=f"Alternativa {alternativas[i]}")
        label_alternativa.grid(row=line_count, column=0, padx=5, pady=5)

        entradas_alternativa = []
        for j in range(len(criterios)):
            label_criterio = ttk.Label(frame, text=f"Criterio: {criterios[j]}")
            label_criterio.grid(row=line_count, column=1, padx=5, pady=5)
            entrada = ttk.Entry(frame)
            entrada.grid(row=line_count, column=2, padx=5, pady=5)
            entradas_alternativa.append(entrada)
            line_count += 1

        entrada_frames.append(entradas_alternativa)

    botao_enviarDados = ttk.Button(janela, text="Enviar valores",
                                   command=lambda: salvar_entradas(alternativas, criterios))
    botao_enviarDados.pack(pady=10)

def salvar_entradas(alternativas, criterios):
    valores_entradas = []

    for i in range(len(alternativas)):
        valores_alternativa = []
        for j in range(len(criterios)):
            valor_entrada = entrada_frames[i][j].get()
            if valor_entrada.strip():
                valor_entrada = str(valor_entrada)
            valores_alternativa.append(valor_entrada)
        valores_entradas.append(valores_alternativa)
    print(f"Dados para cada critério: {valores_entradas}")

    # chamada do codigo do promethee
    promethee_roc(alternativas, criterios, valores_entradas)

# INTERFACE PRINCIPAL
janela = tk.Tk()
janela.title("PROMETHEE II")

frame_criterios = ttk.Frame(janela)
frame_criterios.pack(pady=10)
label_criterios = tk.Label(frame_criterios, text="Informe os critérios\nseparados por vírgula\nem ordem de preferência\n(do mais importante\nao menos importante)")
label_criterios.pack(side=tk.LEFT, padx=5, pady=5)
entry_criterios = ttk.Entry(frame_criterios)
entry_criterios.pack(side=tk.LEFT, padx=5, pady=5)

frame_alternativas = ttk.Frame(janela)
frame_alternativas.pack(pady=10)
label_alternativas = tk.Label(frame_alternativas, text="Informe as alternativas\n(separadas por vírgula)")
label_alternativas.pack(side=tk.LEFT, padx=5, pady=5)
entry_alternativas = ttk.Entry(frame_alternativas)
entry_alternativas.pack(side=tk.LEFT, padx=5, pady=5)

botao_enviar = ttk.Button(janela, text="Enviar", command=enviar_criterios_alternativas)
botao_enviar.pack(pady=10)

frame = ttk.Frame(janela)
frame.pack(pady=10)


entrada_frames = []

janela.mainloop()


