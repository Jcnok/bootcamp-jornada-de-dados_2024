from fastapi import FastAPI, HTTPException
from models import Livro
from sqlmodel import Session, SQLModel, create_engine, select

app = FastAPI()

# Conexão com o banco de dados (SQLite para simplicidade)
DATABASE_URL = "sqlite:///database/biblioteca.db"
engine = create_engine(DATABASE_URL, echo=True)

# Cria as tabelas no banco de dados
SQLModel.metadata.create_all(engine)


@app.post("/livros/")
def adicionar_livro(livro: Livro):
    with Session(engine) as session:
        session.add(livro)
        session.commit()
    return livro


@app.get("/livros/{autor}")
def buscar_livros_por_autor(autor: str):
    with Session(engine) as session:
        livros = session.exec(select(Livro).where(Livro.autor == autor)).all()
        if not livros:
            raise HTTPException(status_code=404, detail="Livros não encontrados")
        return livros


@app.put("/livros/{id_livro}")
def atualizar_disponibilidade_livro(id_livro: int, disponivel: bool):
    with Session(engine) as session:
        livro = session.get(Livro, id_livro)
        if livro is None:
            raise HTTPException(status_code=404, detail="Livro não encontrado")
        livro.disponivel = disponivel
        session.add(livro)
        session.commit()
    return livro


@app.delete("/livros/{id_livro}")
def remover_livro(id_livro: int):
    with Session(engine) as session:
        livro = session.get(Livro, id_livro)
        if livro is None:
            raise HTTPException(status_code=404, detail="Livro não encontrado")
        session.delete(livro)
        session.commit()
    return {"mensagem": "Livro removido com sucesso"}


# Executar o servidor com Uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
