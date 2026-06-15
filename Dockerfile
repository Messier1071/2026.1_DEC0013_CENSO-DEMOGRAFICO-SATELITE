# 1. Pega um Linux levíssimo já com o nosso Python 3.11.9 exato
FROM python:3.12.13-slim

# 2. Cria a pasta 'app' dentro do container e avisa que vamos trabalhar nela
WORKDIR /app

# 3. Copia o arquivo de dependências para dentro da caixa
COPY requirements.txt .

# 4. O "pip install" do container (sem cache para a imagem ficar mais leve)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia o resto do seu projeto (o main.py, as pastas MVC) para dentro
COPY . .

# 6. Libera a porta 8000 da caixa para o mundo exterior
EXPOSE 8000

# 7. O comando que liga o servidor quando a caixa iniciar
# O 0.0.0.0 é vital no Docker: avisa ao FastAPI para aceitar conexões de fora do container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]