# 📊 Análise do Orçamento Público Federal – 2026

## 📌 Visão Geral

Este projeto apresenta um fluxo completo de análise de dados aplicado ao **Orçamento Público Federal de 2026**, simulando um cenário real de trabalho de um Analista de Dados/BI.

O processo foi dividido em três etapas principais:

1. Recebimento do arquivo bruto
2. Tratamento e limpeza com Python
3. Modelagem e visualização no Power BI

---

# 🔄 Pipeline do Projeto

## 🥇 1ª Etapa – Arquivo Bruto

O arquivo original utilizado foi:

```
2026_OrcamentoDespesa.csv
```

Este é o dataset bruto disponibilizado publicamente, contendo:

* 17.272 registros
* 26 colunas
* Valores monetários formatados como texto
* Separadores de milhar (.)
* Vírgula como separador decimal
* Percentuais armazenados como string

Esse formato não estava adequado para análise direta.

---

## 🧹 2ª Etapa – Tratamento e Limpeza com Python

Foi criado o script:

```
main.py
```

Responsável por:

* Ler o arquivo `2026_OrcamentoDespesa.csv`
* Converter colunas monetárias de string para float
* Remover caracteres de formatação (pontos e vírgulas)
* Padronizar tipos de dados
* Calcular métricas agregadas
* Calcular percentual de execução

### 📌 Fórmula utilizada:

```
% Execução = (Orçamento Realizado / Orçamento Atualizado) * 100
```

Após o tratamento, foi gerado um novo arquivo limpo:

```
orcamento_2026_tratado.csv
```

Este novo arquivo passou a conter dados prontos para modelagem e análise.

---

## 🥈 3ª Etapa – Visualização no Power BI

Com o arquivo `orcamento_2026_tratado.csv` já tratado:

* O dataset foi importado no Power BI Desktop
* Foi criado um modelo simples para análise
* Foram desenvolvidas medidas e visualizações

Além disso, foi criado o script:

```
codigo_powerbi.py
```

Este script foi utilizado dentro do **Python Visual do Power BI**, permitindo gerar gráficos personalizados a partir do dataset tratado.

Fluxo dentro do Power BI:

1. Importação do `orcamento_2026_tratado.csv`
2. Inserção de visual Python
3. Utilização do `codigo_powerbi.py`
4. Geração dos gráficos analíticos

---

# 📊 Principais Insights Identificados

* Encargos Especiais concentram o maior volume orçamentário
* Ministério da Fazenda lidera em orçamento atualizado
* Previdência Social ultrapassa 1 trilhão de reais
* Ações relacionadas à dívida pública representam parcela significativa da execução
* A execução orçamentária encontra-se em estágio inicial do exercício

---

# 🚀 Como Executar o Projeto!

## 1️⃣ Clonar o repositório

```
git clone https://github.com/seuusuario/orcamento-publico-2026.git
```

## 2️⃣ Instalar dependências

```
pip install -r requirements.txt
```

## 3️⃣ Executar o tratamento

```
python main.py
```

Isso irá gerar:

```
orcamento_2026_tratado.csv
```

## 4️⃣ Abrir o dashboard

Abrir o arquivo `.pbix` no Power BI Desktop
Ou utilizar o `codigo_powerbi.py` dentro do visual Python.

---

# 💼 Competências Demonstradas

* Limpeza e transformação de dados
* Conversão e padronização de tipos
* Criação de métricas analíticas
* Construção de pipeline de dados
* Integração Python + Power BI
* Comunicação de insights

---

# 🔮 Possíveis Evoluções

* Comparação com anos anteriores
* Análise temporal da execução
* Automatização do pipeline
* Publicação do dashboard online
* Integração com APIs públicas

---

📎 Projeto desenvolvido com foco em portfólio profissional em Análise de Dados e Business Intelligence.
