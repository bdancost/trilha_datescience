# Importar as bibliotecas necessárias
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
ax = sns.barplot(x='Nome do Curso', y='Quantidade de Vendas', data=df)
plt.xticks(rotation=45, ha='right', fontsize=8) 
plt.title('Quantidade de Vendas por Curso')
plt.xlabel('Nome do Curso')
plt.ylabel('Quantidade de Vendas')
plt.tight_layout()

# Adicionar rótulos de dados (labels) no gráfico de barras
for p in ax.patches:
    ax.annotate(f"{p.get_height():.0f}", (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', fontsize=12, color='black', xytext=(0, 5), textcoords='offset points')

plt.show()

sns.set(style='whitegrid', rc={'patch.edgecolor': 'none'})

# Gráfico de dispersão para relação entre variáveis
plt.figure(figsize=(12, 6))
sns.scatterplot(x='Data', y='Quantidade de Vendas', size='Receita', data=df, legend=False, sizes=(20, 200))
plt.title('Quantidade de Vendas ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Quantidade de Vendas')
plt.tight_layout()
plt.show()

# Adicionar rótulos de dados (labels) no gráfico de dispersão
for line in range(0, df.shape[0]):
    ax.text(df['Data'].iloc[line], df['Quantidade de Vendas'].iloc[line], df['Nome do Curso'].iloc[line], horizontalalignment='right', size='medium', color='black', weight='semibold')

plt.show()

