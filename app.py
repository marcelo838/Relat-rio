
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('RECLAMEAQUI_NAGEM.csv')

ano = st.selectbox(
    'ano:',
    df["ANO"].unique()
)
filtered_df = df[df["ANO"] == ano]

filtered_df['TEMPO'] = pd.to_datetime(filtered_df['TEMPO'])

filtered_df.groupby('TEMPO').nunique()['ID'].plot()

# Gráfico de linhas
fig1, ax1 = plt.subplots()
filtered_df.groupby('TEMPO').nunique()['ID'].plot(marker='o', linestyle='-', color='b', label='Número único de IDs', ax=ax1)
ax1.set_title('Número de reclamações por mês durante os anos')
ax1.set_xlabel('Ano')
ax1.set_ylabel('Número de reclamações')
ax1.legend()
ax1.grid(True)
st.pyplot(fig1)

# Gráfico de barras
fig2, ax2 = plt.subplots()
filtered_df['ESTADO'] = filtered_df['LOCAL'].apply(lambda x: x.split('-', 2)[1].strip())
ce_df = filtered_df[filtered_df['ESTADO'] == 'CE']
ce_df.groupby('TEMPO').nunique()['ID'].plot(kind='bar', ax=ax2)
ax2.set_title('Número de reclamações por mês no estado do Ceará')
ax2.set_xlabel('Mês')
ax2.set_ylabel('Número de reclamações')
st.pyplot(fig2)
