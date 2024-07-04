import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados do arquivo CSV
df = pd.read_csv('cursos.csv')

# Exibir as primeiras linhas e informações básicas do conjunto de dados
print("Primeiras linhas do conjunto de dados:")
print(df.head())
print("\nInformações básicas do conjunto de dados:")
print(df.info())

# Calcular e exibir estatísticas descritivas básicas
print("\nEstatísticas descritivas para colunas numéricas:")
print(df.describe())

# Calcular a receita total gerada pela venda dos cursos
df['Receita'] = df['Quantidade de Vendas'] * df['Preço Unitário']
receita_total = df['Receita'].sum()
print(f"\nReceita total gerada pela venda dos cursos: R$ {receita_total:.2f}")

# Identificar o curso com o maior número de vendas
curso_mais_vendido = df.loc[df['Quantidade de Vendas'].idxmax()]
print(f"\nCurso com o maior número de vendas: {curso_mais_vendido['Nome do Curso']} ({curso_mais_vendido['Quantidade de Vendas']} vendas)")

# Visualizar a distribuição das vendas ao longo do tempo
df['Data'] = pd.to_datetime(df['Data'])

# Gráfico de barras para contagem de categorias
plt.figure(figsize=(12, 6))
sns.barplot(x='Nome do Curso', y='Quantidade de Vendas', data=df)
plt.xticks(rotation=90)
plt.title('Quantidade de Vendas por Curso')
plt.show()

# Gráfico de dispersão para relação entre variáveis
plt.figure(figsize=(12, 6))
sns.scatterplot(x='Data', y='Quantidade de Vendas', size='Receita', data=df, legend=False)
plt.title('Quantidade de Vendas ao Longo do Tempo')
plt.show()
