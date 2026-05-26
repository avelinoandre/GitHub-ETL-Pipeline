# 🔄 GitHub ETL Pipeline

> Pipeline ETL automatizada que extrai dados da API REST do GitHub, transforma em DataFrames com Pandas, exporta para `.csv` e realiza o commit dos arquivos em um repositório GitHub — tudo via Python puro com `requests`.

---

## 🔍 Visão Geral

Este projeto implementa uma pipeline ETL (Extract, Transform, Load) completa integrada ao GitHub:

- **Extract** — Requisições HTTP à API REST do GitHub via `requests` para coletar dados (repositórios, issues, pull requests, etc.)
- **Transform** — Processamento e limpeza dos dados com `pandas`, estruturando-os em DataFrames e exportando para arquivos `.csv`
- **Load** — Criação automática de um repositório no GitHub e commit dos arquivos `.csv` gerados, também via `requests`

---

## 🏗 Arquitetura

```
┌─────────────────────────────────────────────────────────────┐
│                      GitHub ETL Pipeline                    │
│                                                             │
│  ┌───────────┐    ┌───────────────┐    ┌────────────────┐  │
│  │  EXTRACT  │───▶│   TRANSFORM   │───▶│      LOAD      │  │
│  │           │    │               │    │                │  │
│  │ GitHub    │    │ pandas        │    │ Cria repo      │  │
│  │ REST API  │    │ DataFrame     │    │ no GitHub      │  │
│  │ requests  │    │ .csv export   │    │ Commit .csv    │  │
│  └───────────┘    └───────────────┘    └────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠 Tecnologias

| Tecnologia | Versão recomendada | Uso |
|---|---|---|
| Python | 3.9+ | Linguagem principal |
| requests | 2.31+ | Requisições HTTP para a API do GitHub |
| pandas | 2.0+ | Transformação e manipulação de dados |

---

## ✅ Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Python 3.9 ou superior** — [Download](https://www.python.org/downloads/)
- **pip** — Gerenciador de pacotes Python (já incluso no Python 3.9+)
- Uma **conta no GitHub** com permissão para criar repositórios
- Um **Personal Access Token (PAT)** do GitHub com os escopos:
  - `repo` (acesso completo a repositórios)
  - `read:user` (leitura de dados do usuário)

### Como gerar um Personal Access Token

1. Acesse [github.com/settings/tokens](https://github.com/settings/tokens)
2. Clique em **"Generate new token (classic)"**
3. Defina um nome descritivo (ex: `etl-pipeline`)
4. Marque os escopos `repo` e `read:user`
5. Clique em **"Generate token"** e salve o token gerado em local seguro

---

## ⚙️ Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/github-etl-pipeline.git
cd github-etl-pipeline
```

### 2. Crie e ative um ambiente virtual

```bash
# Linux / macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```bash
cp .env.example .env
```

Edite o `.env` com suas credenciais:

```env
GITHUB_TOKEN=seu_personal_access_token_aqui
GITHUB_USERNAME=seu_usuario_github
TARGET_REPO_NAME=nome-do-repositorio-de-destino
```

> ⚠️ **Nunca versione o arquivo `.env`**. Ele já está no `.gitignore` por padrão.

---

## 🚀 Como Usar

### Executando a pipeline completa

```bash
python main.py
```

A pipeline irá:

1. Autenticar na API do GitHub com seu token
2. Extrair os dados configurados (repositórios, issues, etc.)
3. Transformar os dados em DataFrames e exportar como `.csv` na pasta `output/`
4. Criar o repositório de destino no GitHub (caso ainda não exista)
5. Fazer o commit de todos os arquivos `.csv` no repositório criado

### Executando etapas individualmente

```bash
# Apenas extração
python pipeline/extract.py

# Apenas transformação
python pipeline/transform.py

# Apenas o carregamento (commit no GitHub)
python pipeline/load.py
```

### Saída esperada

```
[EXTRACT] Buscando dados na API do GitHub...
[EXTRACT] ✔ 42 registros obtidos.

[TRANSFORM] Processando dados com pandas...
[TRANSFORM] ✔ Arquivo salvo: output/repositories.csv

[LOAD] Criando repositório 'etl-output' no GitHub...
[LOAD] ✔ Repositório criado com sucesso.
[LOAD] Realizando commit dos arquivos .csv...
[LOAD] ✔ Commit realizado: repositories.csv → main

Pipeline concluída com sucesso! 🎉
```

---

## 📁 Estrutura do Projeto

```
github-etl-pipeline/
│
├── pipeline/
│   ├── extract.py        # Requisições à API REST do GitHub
│   ├── transform.py      # Transformação com pandas e export .csv
│   └── load.py           # Criação do repositório e commit via API
│
├── output/               # Arquivos .csv gerados (ignorado pelo git)
│
├── main.py               # Ponto de entrada da pipeline
├── requirements.txt      # Dependências do projeto
├── .env.example          # Modelo de variáveis de ambiente
├── .gitignore
└── README.md
```

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<p align="center">
  Desenvolvido com Python 🐍 + GitHub API 🐙
</p>
