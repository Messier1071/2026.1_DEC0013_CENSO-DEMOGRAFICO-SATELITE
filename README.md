# Censo demográfico via satélite

## Visão Geral
Breve descrição do projeto (2-3 parágrafos)

## Requisitos de Software 
- Python, Tkinter e Google Maps static api

## Configuração do Ambiente
- Versões de IDE/toolchain
- Dependências e bibliotecas
- Passo a passo de configuração

## Como Usar
- InstalaçãoÇ
  1. clone o repo do github 
  ~~2. execute o *script* de instalação setup.py~~
  2. crie um *virtual environment* `python -m venv .venv`
  3. execute `.\.venv\Scripts\activate`(windows) ou `commando linux aqui`
  4. `pip install -r .\scripts\requirements.txt`
  5. `python .\src\main.py`
- é necessária uma chave da api do Google e roboflow


## Estrutura do Projeto
O código foi separado em tres partes para simplificar o codesenvolvimento, Model lida com o banco de dados, view lida com a *interface* de usuário e controller interage com APIs externas

## Troubleshooting
TODO

## Contribuidores
- Ian Martins Mendes (23205319) - Organização e Machine Learning
- Lucas Rodrigues da Silva (21205137) - banco de dados e backend de integração
- Pedro Otavio Vaz Alcantara (24103218) - Machine Learning e visão computacional
- Andre de Souza da Costa (23104086) - 

## Estrutura do projeto
```
projeto-software/
├── README.md
├── LICENSE
├── .env                        # chaves de api. Usuario precisa criar e adicionar suas proprias
├── .gitignore
├── .venv/                      # bibliotecas *
├── docs/
│   ├── assets/                 # imagens de referencia
│   ├── boas-praticas.md        # Organização dos dos commits e branches 
│   ├── controller.md           # tarefas e documentacao de cada parte
│   ├── model.md
│   └── view.md
├── src/
│   ├── main.py
│   ├── model/
│   ├── view/
│   └── controller/
├── scripts/                    # scripts de instalação
├── media/                      # imagens salvas pelo programa  *
│   ├── raw/
│   └── controller/
├── database/
│   └──  search_history.sqlite  # *
└── examples/

* criado pelo script de instalação ou em tempo de execução
```

# TODO: refactor code to new standard