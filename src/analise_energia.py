import pandas as pd
import json

# Caminho do arquivo CSV
caminho_csv = 'dados/CONSUMO MENSAL DE ENERGIA ELÉTRICA POR CLASSE.xlsx - CONSUMO RESIDENCIAL POR UF.csv'

# Lê o CSV pulando a linha de cabeçalho inicial e usando as duas primeiras linhas como cabeçalho multi-index
df = pd.read_csv(caminho_csv, sep=',', header=[0, 1], encoding='utf-8', skiprows=4)

# Remove a última linha do DataFrame, pois é uma linha de nota e não representa uma UF
df = df.iloc[:-1]

# Adiciona a coluna 'UF' a partir do índice
df['UF'] = df.iloc[:, 0]  # A primeira coluna é o nome da UF
df = df.drop(columns=df.columns[0])  # Remove a coluna duplicada que foi usada para UF

# Reorganiza para ter a UF como índice e o resto como colunas multi-index (Ano, Mês)
df = df.set_index('UF')

# Converte os dados para float (substitui vírgulas por pontos e transforma em número)
df = df.applymap(lambda x: str(x).replace('.', '').replace(',', '.') if isinstance(x, str) else x)
df = df.apply(pd.to_numeric, errors='coerce')

# Estatísticas simples por estado (soma total, média e desvio padrão)
estatisticas = {}

for estado in df.index:
    dados_estado = df.loc[estado].dropna()
    estatisticas[estado] = {
        'media': round(dados_estado.mean(), 2),
        'soma': round(dados_estado.sum(), 2),
        'desvio_padrao': round(dados_estado.std(), 2)
    }

# Salvar estatísticas em JSON
with open('estatisticas_consumo.json', 'w', encoding='utf-8') as f:
    json.dump(estatisticas, f, ensure_ascii=False, indent=4)

print("Análise estatística salva em 'estatisticas_consumo.json'")
