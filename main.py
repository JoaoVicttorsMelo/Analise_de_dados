import pandas as pd

#criando variavel para ler arquivo .csv
tabela = pd.read_csv("cancelamentos_sample.csv")
#removendo dados sem importância para a verificação
tabela = tabela.drop(columns="CustomerID")

#removendo usuarios com pendencia de cadastro
tabela = tabela.dropna()
print(tabela.info())

#Pegando percentual de cancelamentos
print(tabela["cancelou"].value_counts())
print(tabela["cancelou"].value_counts(normalize=True))

#Pegando percentual de duração do contrato
print(tabela["duracao_contrato"].value_counts())
print(tabela["duracao_contrato"].value_counts(normalize=True))

#fazendo agrupamento de dados de duracao_contrato e cancelou
agrupamento = tabela.groupby("duracao_contrato").mean(numeric_only=True)
print(agrupamento)
