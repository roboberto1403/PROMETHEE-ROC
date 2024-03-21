## promethee_ROC

# Introdução
Em alguns casos de tomada de decisão de problemas de múltiplos critérios há a dificuldade ou impossibilidade de definir os valores para os pesos dos diferentes critérios. Para esses casos, pode-se usar a escala de importância dos critérios para se definir uma ordem de prioridade. DE ALMEIDA FILHO et al. (2018) conclui como o método Rank Order Centroid é o mais robusto entre os mais populares (EW, RS, RR e ROC) para definição de pesos substitutos em problema de tomada de decição multicritéirios. 

# Sobre o projeto
Foi implementado o método Promethee (I e II) utilizando do procedimento ROC em Python e pode ser acessado como uma biblioteca [aqui](https://pypi.org/project/promethee-ROC/0.1/).

# Como utilizar

1. Baixe a biblioteca
```bash
  pip install promethee-ROC
 ```
2. Importe a seguinte função
 ```bash
   from promethee_roc.algoritmo.main import run_promethee_roc
   ```
4. Execute a função run_promethe_roc
   ```bash
   run_promethee_roc()
   ```
5. Siga as instruções, após isso, irá ter como retorno as Classificações Parcial (Promethee I) e Total (Promethee II) (BRANS; MARESCHAL, 2005).

# Limitações
Os índices de preferência são calculados utilizando uma função limiar e a lógica do algoritmo apenas suporta critérios de maximazação (quanto maior, melhor), de forma que, caso o usuário deseje utilizar de critério de minimização, deverá manualmente normalizar os valores (multiplicando todos por 1/x*2, sendo x o valor do critério).

# Equipe
* Luana Cristina de Carvalho Brito <lccb@cin.ufpe.br>
* Gabrielle Almeida de Oliveira <gao2@cin.ufpe.br>
* Luiz Roberto Bezerra Ferreira <rbf@cin.ufpe.br>
* Penélope Araújo <pmpa@cin.ufpe.br>
* Joao Felipe Barbosa da Silva <jfbs@cin.ufpe.br>

# Referências
BRANS, J.-P.; MARESCHAL, B. Promethee Methods. International Series in Operations Research & Management Science, p. 163–186, 2005.

DE ALMEIDA FILHO, A. T. et al. Preference modeling experiments with surrogate weighting procedures for the PROMETHEE method. European Journal of Operational Research, v. 264, n. 2, p. 453–461, jan. 2018.
