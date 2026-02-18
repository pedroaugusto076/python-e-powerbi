import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import textwrap

plt.rcParams["font.family"] = "DejaVu Sans"

df = dataset.copy()

# Converter valores
df["ORÇAMENTO ATUALIZADO (R$)"] = (
    df["ORÇAMENTO ATUALIZADO (R$)"]
    .astype(str)
    .str.replace(".", "", regex=False)
    .str.replace(",", ".", regex=False)
    .astype(float)
)

# Agrupar
top_orgaos = (
    df.groupby("NOME ÓRGÃO SUPERIOR")["ORÇAMENTO ATUALIZADO (R$)"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# Quebrar textos longos
labels = [
    "\n".join(textwrap.wrap(nome, 30))
    for nome in top_orgaos.index
]

# Criar gráfico
fig, ax = plt.subplots(figsize=(7,6), dpi=120)

ax.barh(labels, top_orgaos.values)

ax.set_title(
    "Top 10 Órgãos por Orçamento Atualizado - 2026",
    fontsize=10,
    weight="bold"
)

ax.invert_yaxis()

# Formatar eixo X
def formatar_moeda(x, pos):
    return f"R$ {x/1_000_000_000:.1f} Bi"

ax.xaxis.set_major_formatter(ticker.FuncFormatter(formatar_moeda))

ax.tick_params(axis='y', labelsize=8)
ax.tick_params(axis='x', labelsize=8)

ax.grid(axis='x', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()
