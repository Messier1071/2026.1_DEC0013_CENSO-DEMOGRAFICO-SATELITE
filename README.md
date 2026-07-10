# Censo demográfico via satélite 🛰️🌍
## 📖 Visão Geral
Este projeto é um sistema desktop desenvolvido para estimar a população de uma determinada região geográfica utilizando imagens de satélite. Através da integração com a API estática do Google Maps, o sistema captura recortes do mapa e utiliza modelos de Inteligência Artificial (via Roboflow) para identificar construções e telhados, realizando cálculos demográficos de forma automatizada.

O código foi separado em três partes principais para simplificar o desenvolvimento (arquitetura MVC): o **Model** lida com a persistência no banco de dados, o **View** lida com a interface de usuário e o **Controller** interage com as APIs externas e processamento de dados.

<br>

## 💻 Pré-requisitos
* Python 3.11
* Biblioteca Tkinter (geralmente incluída na instalação padrão do Python)
* Chave da API do Google Maps (Maps Static API)
* Chave da API do Roboflow (Inference SDK)

<br>

## 🚀 Configuração do Ambiente e Como Rodar

**1. Clone o repositório do GitHub:**
```bash
git clone https://github.com/Messier1071/2026.1_DEC0013_CENSO-DEMOGRAFICO-SATELITE.git
cd 2026.1_DEC0013_CENSO-DEMOGRAFICO-SATELITE
```

**2. Crie e ative um ambiente virtual (virtual environment):**
```bash
python -m venv .venv

# No Windows:
.\.venv\Scripts\activate

# No Linux/macOS:
source .venv/bin/activate
```

**3. Instale as dependências:**
```bash
pip install -r .\scripts\requirements.txt
```

**4. Configure as chaves de API:**
Crie um arquivo `.env` na raiz do projeto e adicione as suas chaves:
```env
GOOGLE_MAPS_API_KEY=sua_chave_aqui
ROBOFLOW_API_KEY=sua_chave_aqui
```

**5. Execute a aplicação:**
```bash
python .\src\main.py
```

## 📚 Tutorial de Uso
Quer ver o sistema em ação na prática? Preparamos um guia passo a passo completo para o ajudar a realizar a sua primeira estimativa demográfica, desde a seleção das coordenadas da área até à visualização final dos resultados gerados pela IA.

👉 **[Clique aqui para acessar o Tutorial de Uso](docs/tutorial.md)**

<br>

## 📂 Estrutura do Projeto
```text
2026.1_DEC0013_CENSO-DEMOGRAFICO-SATELITE/
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
```
*\* Criado pelo script de instalação ou em tempo de execução.*

<br>

## 🐛 Troubleshooting
* **TODO**

<br>

## 👥 Contribuidores
* **Ian Martins Mendes** (23205319) - Organização e Machine Learning
* **Lucas Rodrigues da Silva** (21205137) - Banco de dados e backend de integração
* **Pedro Otavio Vaz Alcantara** (24103218) - Machine Learning e visão computacional
* **Andre de Souza da Costa** (23104086) - Interface gráfica e UX