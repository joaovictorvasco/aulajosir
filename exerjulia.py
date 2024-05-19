import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Casos de Zika recebidos na Colômbia em 2016')

# Carregar o arquivo CSV
df = pd.read_csv('colombia-2016-01-22.csv')

# Exibir o DataFrame
st.write("DataFrame:")
st.write(df)

# Gerar o gráfico
fig, ax = plt.subplots(figsize=(10, 5))
df.plot(kind='bar', x='region', y='samples_received', ax=ax)
ax.set_xlabel("Regiões")
ax.set_ylabel("Casos")
ax.set_title('Casos de Zika recebidos na Colômbia em 2016')
ax.spines[['top', 'right']].set_visible(False)

# Exibir o gráfico
st.pyplot(fig)
