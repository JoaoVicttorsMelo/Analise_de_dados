import pandas as pd

tabela = pd.read_csv("cancelamentos_sample.csv")
tabela = tabela.drop(columns="CustomerID")
print(tabela.info())