import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Função para carregar os dados
@st.cache_data
def load_data():
    input_path = 'E:/Coins/planilha_atualizada.xlsx'
    df = pd.read_excel(input_path, sheet_name='Carteira')
    return df

# Carregar os dados
df_carteira = load_data()

# Calcular informações principais
total_investido = df_carteira['Valor Investido'].sum()
total_lucro = df_carteira['Lucro R$'].sum()
total_ativo = df_carteira['Total'].sum()

# Configurar o layout do Streamlit
st.title('Dashboard de Carteira de Criptomoedas')

# Cartões com informações principais
st.header('Informações Principais')

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label='Lucro Total (R$)', value=f'R$ {total_lucro:,.2f}', delta=f'R$ {total_lucro:,.2f}')
with col2:
    st.metric(label='Total Investido (R$)', value=f'R$ {total_investido:,.2f}', delta=f'R$ {total_investido:,.2f}')
with col3:
    st.metric(label='Total que Possui (R$)', value=f'R$ {total_ativo:,.2f}', delta=f'R$ {total_ativo:,.2f}')

# Gráfico de pizza do valor investido por criptomoeda
st.header('Valor Investido por Criptomoeda')
fig = px.pie(df_carteira, names='Cripto', values='Valor Investido', title='Distribuição do Valor Investido por Criptomoeda')
st.plotly_chart(fig)

# Gráfico de colunas (barras) do lucro R$ por criptomoeda
st.header('Lucro R$ por Criptomoeda (Gráfico de Colunas)')
fig = px.bar(df_carteira, x='Cripto', y='Lucro R$', title='Lucro R$ por Criptomoeda', labels={'Lucro R$': 'Lucro R$'})
st.plotly_chart(fig)

# Gráfico de Total por Criptomoeda (Barra)
st.header('Total por Criptomoeda')
fig = px.bar(df_carteira, x='Cripto', y='Total', title='Total por Criptomoeda', labels={'Total': 'Total (R$)'})
st.plotly_chart(fig)

# Gráfico de Lucro %R$ por Criptomoeda (Barra)
st.header('Lucro %R$ por Criptomoeda')
fig = px.bar(df_carteira, x='Cripto', y='Lucro %R$', title='Lucro %R$ por Criptomoeda', labels={'Lucro %R$': 'Lucro %R$'})
st.plotly_chart(fig)