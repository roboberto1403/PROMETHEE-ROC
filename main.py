from promethee import calcular_fluxos, ordenar_alternativas

def main(criterios, alternativas, dados):
    criterios_com_pesos = []
    somatorio = 0
    for i in range(len(criterios)-1, -1, -1):
        criterios_com_pesos.append((f"{criterios[i]}", 1/len(criterios) * (somatorio + 1/(i+1))))
        somatorio += 1/(i+1)
    criterios_com_pesos.reverse()

    fluxos_totais, fluxos_positivos, fluxos_negativos, indices = calcular_fluxos(alternativas, criterios_com_pesos, dados)
    alternativas_ordenadas = ordenar_alternativas(alternativas, fluxos_totais)
    print(criterios_com_pesos)
    print(fluxos_positivos)
    print(fluxos_negativos)
    print(indices)

    print("\nRanking das Alternativas:")
    for i, (alternativa, fluxo) in enumerate(alternativas_ordenadas, 1):
        print(f"{i}. {alternativa}: {fluxo}")

c = ["c1", "c3", "c2"]
a = ["a1", "a2", "a3"]
dados = [
    [10, 20, 30],
    [15, 25, 35],
    [12, 18, 25]
]
if __name__ == "__main__":
    main(c, a, dados)


