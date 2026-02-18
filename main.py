# main.py
# Projeto: Análise de Orçamento de Despesa 2026
# Autor: Você
# Objetivo: Limpar, tratar, gerar insights e gráficos

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 1️⃣ Abrir arquivo CSV
# -------------------------------
df = pd.read_csv(
    "2026_OrcamentoDespesa.csv",
    sep=";",
    encoding="latin1"
)

# -------------------------------
# 2️⃣ Converter colunas de valor para float
# -------------------------------
colunas_valor = [
    "ORÇAMENTO INICIAL (R$)",
    "ORÇAMENTO ATUALIZADO (R$)",
    "ORÇAMENTO EMPENHADO (R$)",
    "ORÇAMENTO REALIZADO (R$)",
    "% REALIZADO DO ORÇAMENTO (COM RELAÇÃO AO ORÇAMENTO ATUALIZADO)"
]

for col in colunas_valor:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
        .str.replace("%", "", regex=False)
        .astype(float)
    )

# -------------------------------
# 3️⃣ Informações básicas
# -------------------------------
print("Número de linhas e colunas:", df.shape)
print("\nTipos de colunas e nulos:")
print(df.info())
print("\n10 primeiras linhas:")
print(df.head(10))

# -------------------------------
# 4️⃣ Top 10 Órgãos por Orçamento Atualizado
# -------------------------------
top_orgaos = (
    df.groupby("NOME ÓRGÃO SUPERIOR")["ORÇAMENTO ATUALIZADO (R$)"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print("\nTop 10 Órgãos por Orçamento Atualizado:")
print(top_orgaos)

# -------------------------------
# 5️⃣ Eficiência: % do orçamento realizado
# -------------------------------
execucao = df.groupby("NOME ÓRGÃO SUPERIOR")[[
    "ORÇAMENTO ATUALIZADO (R$)",
    "ORÇAMENTO REALIZADO (R$)"
]].sum()

execucao["% EXECUTADO"] = (
    execucao["ORÇAMENTO REALIZADO (R$)"] /
    execucao["ORÇAMENTO ATUALIZADO (R$)"]
) * 100

execucao = execucao.sort_values("% EXECUTADO", ascending=False)
print("\nTop 10 Órgãos por % de execução do orçamento:")
print(execucao.head(10))

# -------------------------------
# 6️⃣ Orçamento por Função
# -------------------------------
orcamento_funcao = (
    df.groupby("NOME FUNÇÃO")["ORÇAMENTO ATUALIZADO (R$)"]
    .sum()
    .sort_values(ascending=False)
)
print("\nOrçamento por Função:")
print(orcamento_funcao)

# -------------------------------
# 7️⃣ Orçamento por Grupo de Despesa
# -------------------------------
orcamento_grupo = (
    df.groupby("NOME GRUPO DE DESPESA")["ORÇAMENTO ATUALIZADO (R$)"]
    .sum()
    .sort_values(ascending=False)
)
print("\nOrçamento por Grupo de Despesa:")
print(orcamento_grupo)

# -------------------------------
# 8️⃣ Top 10 Ações por execução
# -------------------------------
top_acoes = (
    df.groupby("NOME AÇÃO")["ORÇAMENTO REALIZADO (R$)"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print("\nTop 10 Ações por execução:")
print(top_acoes)

# -------------------------------
# 9️⃣ Gráficos
# -------------------------------
plt.style.use('ggplot')

# Gráfico 1: Top 10 órgãos por orçamento atualizado
top_orgaos.plot(kind='barh', figsize=(10,6), color='skyblue')
plt.title("Top 10 Órgãos por Orçamento Atualizado (R$)")
plt.xlabel("R$ Atualizado")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# Gráfico 2: % execução por órgão
execucao['% EXECUTADO'].head(10).plot(kind='barh', figsize=(10,6), color='orange')
plt.title("% Execução do Orçamento - Top 10 Órgãos")
plt.xlabel("% Executado")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# Gráfico 3: Orçamento por Função (Top 10)
orcamento_funcao.head(10).plot(kind='barh', figsize=(10,6), color='green')
plt.title("Top 10 Funções por Orçamento Atualizado (R$)")
plt.xlabel("R$ Atualizado")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# -------------------------------
# 10️⃣ Exportar CSV limpo para Power BI
# -------------------------------
df.to_csv(r"C:\Users\userp\Documents\powerbi\orcamento_2026_tratado.csv", index=False)
print("✅ CSV tratado gerado com sucesso em: C:\\Users\\userp\\Documents\\powerbi\\orcamento_2026_tratado.csv")
