from google.colab import drive

drive.mount('/content/drive')

import pandas as pd

dados_v = pd.read_csv('/content/drive/My Drive/Colab Notebooks/venda.csv')
dados_v.head()

vendas_mes = input('Qual Mês você quer analisar? ' )

analise = dados_v.sort_values(by=f'{vendas_mes}', ascending=False)
print(analise)

novos_funcionarios = pd.DataFrame({'Funcionarios': ['Hilton', 'Beatriz'],
'Janeiro': [85, 62],
'Fevereiro': [56, 41],
'Março': [95, 38]})

dados_atualizados = pd.concat([dados_v, novos_funcionarios], ignore_index=True)
dados_atualizados.to_csv('/content/drive/My Drive/Colab Notebooks/venda.csv', index=False)
print(dados_v)