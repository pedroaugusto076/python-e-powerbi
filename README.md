# 📊 Análise do Orçamento Público Federal – 2026

## 📌 Visão Geral

Este projeto tem como objetivo realizar uma análise exploratória do **Orçamento Público Federal de 2026**, aplicando um fluxo completo de análise de dados:

1. **Tratamento e preparação dos dados com Python**
2. **Modelagem e construção de dashboard no Power BI**

O projeto simula um cenário real de trabalho de um Analista de Dados/BI, onde os dados brutos precisam ser tratados antes de serem utilizados em visualizações estratégicas.

---

# 🔄 Pipeline do Projeto

## 🥇 Etapa 1 – Tratamento de Dados com Python

O arquivo CSV original continha:

* Valores monetários formatados como texto
* Separadores de milhar (.)
* Vírgulas como separador decimal
* Colunas categóricas extensas
* Necessidade de agregações e cálculos adicionais

### 🔧 Processos realizados:

* Leitura do CSV com pandas
* Conversão das colunas monetárias de string para float
* Remoção de caracteres de formatação
* Padronização dos dados
* Criação de métricas agregadas
* Cálculo do percentual de execução orçamentária

### 📌 Exemplo de cálculo:

```
% Execução = (Orçamento Realizado / Orçamento Atualizado) * 100
```

Após o tratamento, os dados ficaram prontos para análise e visualização.

---

## 🥈 Etapa 2 – Modelagem e Dashboard no Power BI

Com os dados tratados:

* Importação do dataset limpo no Power BI
* Criação de medidas DAX para cálculos dinâmicos
* Construção de ranking de órgãos por orçamento
* Análise por função governamental
* Análise por grupo de despesa
* Comparação entre orçamento atualizado e realizado
* Visualização da execução percentual

### 🎯 Objetivo do Dashboard

Permitir que o usuário:

* Identifique onde o orçamento está concentrado
* Analise o nível de execução
* Compare categorias de despesa
* Explore dados de forma interativa

---

# 🛠️ Ferramentas Utilizadas

* **Python**

  * pandas
  * matplotlib
* **Power BI**
* Git
* GitHub

---

# 📂 Estrutura do Projeto

```
orcamento-publico-2026/
│
├── data/
│   └── 2026_OrcamentoDespesa.csv
│
├── scripts/
│   └── main.py
│
├── dashboard/
│   └── dashboard.pbix
│
├── README.md
└── requirements.txt
```

---

# 📊 Principais Insights Identificados

* Encargos Especiais concentram o maior volume orçamentário
* Ministério da Fazenda lidera em orçamento atualizado
* Previdência Social ultrapassa a marca de 1 trilhão de reais
* Ações relacionadas à dívida pública representam parcela significativa da execução
* A execução orçamentária ainda está em estágio inicial do exercício

---

# 🚀 Como Executar o Projeto

### 1️⃣ Clonar o repositório

```
git clone https://github.com/seuusuario/orcamento-publico-2026.git
```

### 2️⃣ Instalar dependências

```
pip install -r requirements.txt
```

### 3️⃣ Executar tratamento

```
python main.py
```

### 4️⃣ Abrir o dashboard

Abrir o arquivo `.pbix` no Power BI Desktop.

---

# 💼 Competências Demonstradas

* Limpeza e transformação de dados
* Manipulação de grandes volumes de dados
* Análise exploratória
* Construção de indicadores
* Business Intelligence
* Comunicação de dados

---

# 🔮 Possíveis Evoluções

* Comparação com anos anteriores
* Análise temporal da execução
* Automação do pipeline de dados
* Criação de relatórios automatizados
* Integração com APIs públicas

---

📎 Projeto desenvolvido para fins de estudo e portfólio em Análise de Dados e Business Intelligence.
