import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Função para carregar e processar os dados
def load_data():
    try:
        df = pd.read_csv('drivers.csv')
        if df.empty:
            st.error("O arquivo CSV está vazio.")
            return None
        grouped_df = df.groupby('Nationality')['PTS'].sum().reset_index()
        grouped_df = grouped_df.sort_values(by='PTS', ascending=False)
        return grouped_df
    except FileNotFoundError:
        st.error("Arquivo 'drivers.csv' não encontrado.")
        return None
    except pd.errors.EmptyDataError:
        st.error("O arquivo 'drivers.csv' está vazio.")
        return None
    except pd.errors.ParserError:
        st.error("Erro ao analisar o arquivo 'drivers.csv'. Verifique se o arquivo está no formato correto.")
        return None

# Função para criar o gráfico
def create_bar_chart(data):
    if data is not None:
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        sns.barplot(x='PTS', y='Nationality', data=data, palette='viridis')
        plt.title('Total de Pontos por Nacionalidade')
        plt.xlabel('Pontos')
        plt.ylabel('Nacionalidade')
        st.pyplot(plt)

# Carregar os dados
data = load_data()

# Criar o título da aplicação
st.title('Análise de Pontos por Nacionalidade')

# Mostrar o gráfico
create_bar_chart(data)
