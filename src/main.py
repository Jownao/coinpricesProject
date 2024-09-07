import pandas as pd
import warnings
from funcs import get_usd_to_brl, get_crypto_price

warnings.filterwarnings("ignore", category=UserWarning, module='openpyxl')

# Caminhos dos arquivos
input_path = 'E:/Coins/planilha_raiz.xlsx'
output_path = 'E:/Coins/planilha_atualizada.xlsx'



# Ler a planilha
try:
    df_carteira = pd.read_excel(input_path, sheet_name='Carteira')
    print('Planilha carregada com sucesso!')
except Exception as e:
    print(f'Erro ao carregar a planilha: {e}')

try:
    # Ler a planilha
    df_carteira = pd.read_excel(input_path, sheet_name='Carteira')

    # Ler a planilha de operações
    df_operacoes = pd.read_excel(input_path, sheet_name='Operações')

    # Obter a cotação do USD em BRL
    fake_data = False  # Defina como False para usar dados reais
    usd_to_brl = get_usd_to_brl(fake=fake_data)

    # Calcular o total das taxas por criptomoeda
    df_operacoes['Cripto'] = df_operacoes['CRIPTO']
    taxas_totais = df_operacoes.groupby('Cripto')['TAXA'].sum().reset_index()
    taxas_totais.columns = ['Cripto', 'Custos Taxas']

    # Mesclar as taxas com o DataFrame da carteira
    df_carteira = df_carteira.merge(taxas_totais, on='Cripto', how='left')
    df_carteira.drop('Custos Taxas_x', axis= 1, inplace=True)

    # Atualizar os preços das criptomoedas em USD
    df_carteira['Cotação USD'] = df_carteira['Cripto'].apply(get_crypto_price, currency='usd',fake=fake_data)

    # Atualizar os preços das criptomoedas em BRL
    df_carteira['Cotação BRL'] = df_carteira['Cotação USD'] * usd_to_brl
    
    #print(df_carteira.head())
    
    # Calcular os valores na planilha
    df_carteira['PM R$'] = df_carteira['Valor Investido'] / df_carteira['QTD']
    df_carteira['Total'] = df_carteira['Cotação BRL'] * df_carteira['QTD']
    df_carteira['Custos Taxas'] = df_carteira['Custos Taxas_y']
    df_carteira['Lucro R$'] = df_carteira['Total'] - df_carteira['Valor Investido']
    df_carteira['Lucro %R$'] = (df_carteira['Lucro R$'] / df_carteira['Valor Investido']) * 100
    df_carteira['Lucro $'] = df_carteira['Lucro R$'] / usd_to_brl
    df_carteira['Lucro %$'] = (df_carteira['Lucro $'] / (df_carteira['Valor Investido'] / usd_to_brl)) * 100

    # Salvar as alterações
    df_carteira.to_excel(output_path, sheet_name='Carteira', index=False)
    print("Planilha atualizada com sucesso!")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

