# Use a imagem oficial do Python 3.11
FROM python:3.11

# Define o diretório de trabalho no container
WORKDIR /app

# Instala o virtualenv
RUN pip install virtualenv

# Cria e ativa o ambiente virtual
RUN virtualenv venv
RUN . venv/bin/activate

# Copia os arquivos necessários para o container
COPY requirements.txt .
COPY app.py .

# Instala as dependências dentro do ambiente virtual
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta em que a API estará rodando
EXPOSE 5000

# Comando para executar a aplicação
CMD ["python", "app.py"]