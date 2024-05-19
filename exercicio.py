import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Função para carregar e processar os dados
def load_data():
    df = pd.read_csv('drivers.csv')
    grouped_df = df.groupby('Nationality')['PTS'].sum().reset_index()
    grouped_df = grouped_df.sort_values(by='PTS', ascending=False)
    return grouped_df

# Função para criar o gráfico
def create_bar_chart(data):
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

