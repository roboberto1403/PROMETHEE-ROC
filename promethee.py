def calcular_indices_preferencia(alternativa1, alternativa2, criterios, alternativas, dados):
    indice_preferencia = 0
    for j in range(len(criterios)):
        indice = 0
        if dados[alternativas.index(alternativa1)][j] > dados[alternativas.index(alternativa2)][j] > 0:
            indice = 1 - (dados[alternativas.index(alternativa2)][j] / dados[alternativas.index(alternativa1)][j])
        elif dados[alternativas.index(alternativa1)][j] <= dados[alternativas.index(alternativa2)][j]:
            indice = 0
        elif dados[alternativas.index(alternativa2)][j] == 0:
            indice = 1
        indice_preferencia += indice * criterios[j][1]
    return indice_preferencia


def calcular_fluxos(alternativas, criterios, dados):
    pares = [(a, b) for a in alternativas for b in alternativas if a != b]
    todos_indices = {}
    todos_fluxos_positivos = {}
    todos_fluxos_negativos = {}

    for par in pares:
        indice_par = calcular_indices_preferencia(par[0], par[1], criterios, alternativas, dados)
        todos_indices[f"Indice({par[0]}, {par[1]})"] = indice_par

    for alternativa in alternativas:
        soma_indice_positivo = 0
        for par, indice in todos_indices.items():
            if par.startswith(f"Indice({alternativa}"):
                soma_indice_positivo += indice
        fluxo_positivo = 1 / (len(alternativas) - 1) * soma_indice_positivo
        todos_fluxos_positivos[f"Fluxo positivo {alternativa}"] = fluxo_positivo

        soma_indice_negativo = 0
        for par, indice in todos_indices.items():
            if par.endswith(f"{alternativa})"):
                soma_indice_negativo += indice
        fluxo_negativo = 1 / (len(alternativas) - 1) * soma_indice_negativo
        todos_fluxos_negativos[f"Fluxo negativo {alternativa}"] = fluxo_negativo

    todos_fluxos_totais = {}
    for alternativa in alternativas:
        todos_fluxos_totais[f"Fluxo total {alternativa}"] = todos_fluxos_positivos[f"Fluxo positivo {alternativa}"] - todos_fluxos_negativos[f"Fluxo negativo {alternativa}"]

    return todos_fluxos_totais, todos_fluxos_positivos, todos_fluxos_negativos, todos_indices


def ordenar_alternativas(alternativas, fluxos_totais):
    alternativas_ordenadas = sorted(fluxos_totais.items(), key=lambda x: x[1], reverse=True)
    return alternativas_ordenadas
