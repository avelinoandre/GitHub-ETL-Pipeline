# Pipeline ETL c/ API Rest do GitHub

Este projeto é uma pipeline de **ETL (Extract, Transform, Load)** desenvolvida em Python. O objetivo principal é consumir a API REST do GitHub para identificar, extrair e analisar as principais linguagens de programação adotadas por grandes organizações (como Amazon, Apple, Netflix, Spotify, entre outras), mapeando suas preferências tecnológicas com base em seus repositórios públicos.

O grande diferencial desta pipeline é a arquitetura de separação: após processar as informações, a pipeline cria, atualiza e commita de forma automatizada os resultados em um **repositório secundário focado exclusivamente no armazenamento de dados (CSV)**, mantendo o código-fonte isolado dos datasets.

---

## ⚙️ Como a Pipeline Funciona

A arquitetura do projeto segue o fluxo tradicional de engenharia de dados:

* **Extração (Extract):** Utiliza a biblioteca `requests` para fazer requisições autenticadas aos endpoints da API REST do GitHub, coletando dados brutos sobre os repositórios das empresas selecionadas.
* **Transformação (Transform):** Os dados coletados são tratados utilizando a biblioteca `pandas`. O script limpa inconsistências, analisa a volumetria e relevância de cada linguagem de programação por organização e estrutura as informações em DataFrames limpos.
* **Carga (Load):** Os DataFrames consolidados são exportados para arquivos `.csv`. Em seguida, a pipeline interage com o ecossistema Git para criar e commitar esses arquivos diretamente em um repositório focado apenas em *Data Storage*.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x** - Linguagem core do projeto.
* **Requests** - Para consumo, paginação e tratamento de requisições da API do GitHub.
* **Pandas** - Para manipulação, limpeza, pivotagem e estruturação analítica dos dados.
* **Git Automation** - Para deploy automatizado dos dados gerados para o repositório de destino.

---

## 📁 Estrutura do Projeto

* `application.py`: Ponto de entrada que orquestra a execução da pipeline.
* `models/DataRepository.py`: Módulo responsável pela lógica de extração e transformação analítica com Pandas.
* `models/ToRepository.py`: Módulo responsável pela automação de carga e versionamento dos arquivos CSV no repositório de dados.
* `linguagens_repo.ipynb`: Notebook Jupyter utilizado para prototipagem e análise exploratória inicial das requisições.
