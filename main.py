import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import time


# Definindo uma classe para análise de cancelamentos
class AnaliseCancelamento:
    def __init__(self, csv_file):
        # Lê o arquivo CSV e armazena os dados na tabela
        self.tabela = pd.read_csv(csv_file)
        self.limpar_dados()  # Executa a limpeza inicial dos dados

    # Método privado para limpar os dados
    def limpar_dados(self):
        # Remove a coluna "CustomerID"
        self.tabela = self.tabela.drop(columns="CustomerID")
        # Remove linhas com valores nulos
        self.tabela = self.tabela.dropna()
        # Remove entradas mensais, pois todos os mensais cancelaram
        self.tabela = self.tabela[self.tabela["duracao_contrato"] != "Monthly"]
        # Filtra entradas com menos de 5 ligações para o callcenter e menos de 20 dias de atraso
        self.tabela = self.tabela[self.tabela["ligacoes_callcenter"] < 5]
        self.tabela = self.tabela[self.tabela["dias_atraso"] <= 20]

    # Método para analisar cancelamentos
    def analise_cancelamento(self):
        print("Analise de Cancelamento:")
        # Imprime a contagem de cancelamentos
        print(self.tabela["cancelou"].value_counts())
        # Imprime a porcentagem de cancelamentos
        print(self.tabela["cancelou"].value_counts(normalize=True))

    # Método para gerar histogramas
    def gerar_histograma(self):
        print("Gerando Histogramas:")
        # Loop pelas colunas da tabela
        for coluna in self.tabela.columns:
            time.sleep(3)  # Delay para visualização
            # Cria um histograma com a coluna e cores para cancelamentos
            grafico = px.histogram(self.tabela, x=coluna, color="cancelou")
            grafico.show()

    # def Gerar_grafico_pizza(self):
    #     print("Gerando Graficos de Pizza:")
    #     # Loop pelas colunas da tabela
    #     for coluna in self.tabela.columns:
    #         time.sleep(3)  # Delay para visualização
    #         # Cria um gráfico de pizza com a coluna e cores para cancelamentos
    #         fig = px.pie(self.tabela, names=coluna, title=coluna, hole=0.3)
    #         fig.show()


if __name__ == "__main__":
    # Cria uma instância da classe CancelamentoAnalyzer com o arquivo CSV
    analise = AnaliseCancelamento("cancelamentos_sample.csv")
    # Executa a análise de cancelamentos
    analise.analise_cancelamento()
    # Gera os histogramas
    analise.gerar_histograma()
