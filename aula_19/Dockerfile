FROM python:3.10.13

# Instalando o Poetry
RUN pip install poetry

# Copiar o conteúdo do diretório atual para o contêiner
COPY . /aula19

# Definir o diretório de trabalho
WORKDIR /aula19

# Instalar as dependências do projeto com Poetry
RUN poetry install

# Definir o diretório de trabalho
WORKDIR ./src

# Expor a porta em que a aplicação estará escutando
EXPOSE 8501

# Definir o entrypoint para executar o servidor Uvicorn
ENTRYPOINT ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8501"]
