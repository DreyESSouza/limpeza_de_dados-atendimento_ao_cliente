# 🧹 Limpeza e Tratamento de Dados de Atendimento ao Cliente com Python

## 📌 Sobre o Projeto

Este projeto tem como objetivo realizar a limpeza, padronização e validação de uma base de dados de atendimento ao cliente contendo mais de 80 mil registros.

A base utilizada apresenta diversos problemas comuns encontrados em ambientes corporativos, como valores ausentes, registros duplicados, inconsistências de formatação, erros de digitação, categorias padronizadas incorretamente e dados inválidos.

O processo foi desenvolvido utilizando Python e a biblioteca Pandas, seguindo boas práticas de Data Cleaning para preparar os dados para futuras análises e visualizações.

---

## 🛠️ Tecnologias Utilizadas

* Python
* Pandas
* NumPy

---

## 📊 Estrutura da Base de Dados

A base contém informações relacionadas ao atendimento ao cliente, incluindo:

* Identificação do chamado
* Data de abertura
* Dados do cliente
* Canal de atendimento
* Produto ou serviço
* Tipo de problema
* Prioridade
* Status do chamado
* Tempo de resposta
* Tempo de resolução
* Satisfação do cliente
* Região geográfica

---

## 🔍 Problemas Identificados

Durante a análise da base foram encontrados diversos problemas de qualidade de dados:

* Registros duplicados
* Valores ausentes
* Datas inválidas
* IDs inconsistentes
* Categorias escritas de formas diferentes
* Caracteres especiais indevidos
* Valores numéricos negativos
* Idades fora da faixa aceitável
* Cidade e estado armazenados em colunas incorretas
* Diferenças de capitalização (maiúsculas e minúsculas)

---

## ⚙️ Tratamentos Realizados

### Limpeza Geral

* Remoção de registros duplicados
* Conversão de valores inválidos para nulos (`NaN`)
* Padronização de texto
* Conversão automática de tipos de dados

### Padronização de Identificadores

* Correção de formatos inconsistentes no campo `ticket_id`
* Padronização de identificadores de clientes

### Tratamento de Datas

* Conversão da coluna `created_at` para formato datetime
* Identificação automática de datas inválidas

### Padronização de Categorias

Foram padronizadas categorias como:

* Região
* Canal de atendimento
* Produto
* Tipo de problema
* Prioridade
* Status
* Sentimento do cliente

Utilizando expressões regulares para corrigir variações e erros de digitação.

### Validação Numérica

* Remoção de valores negativos
* Conversão de dados inválidos para nulos
* Validação de idade entre 18 e 100 anos
* Validação das notas de satisfação

### Correção Geográfica

* Identificação de registros onde cidade e estado estavam invertidos
* Correção automática das colunas

---

## 📈 Resultados

Após o processo de limpeza, a base tornou-se adequada para:

* Análise exploratória de dados (EDA)
* Construção de dashboards
* Geração de indicadores
* Modelagem estatística
* Projetos de Business Intelligence

---

## 📂 Estrutura do Projeto

```text
├── Base_de_Dados.csv
├── tratando_base.py
├── Base_de_Dados_tratada.csv
└── README.md
```

---

## 🚀 Possíveis Análises Futuras

Com a base tratada é possível realizar análises como:

* Regiões com maior volume de chamados
* Principais tipos de reclamação
* Tempo médio de resolução
* Satisfação dos clientes
* Desempenho por canal de atendimento
* Distribuição geográfica dos atendimentos
* Relação entre prioridade e tempo de resolução

---

## 👨‍💻 Autor

Projeto desenvolvido por Andrey Souza como parte dos estudos e desenvolvimento de portfólio na área de Análise de Dados.
