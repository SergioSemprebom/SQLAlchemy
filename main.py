from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base


db  = create_engine("sqlite:///SQLite.db")
Session = sessionmaker(bind=db)
session = Session() # sessao que irei usar

Base = declarative_base() # é a transformacao do sql para python
Base.metadata.create_all(bind=db) # cria todos as tabelas 

# criando as tabelas
class Usuario(Base):
    __tablename__ = "usuarios" # 15:00 estou determinando o nome da tabela como usuario

    id =    Column("id", Integer, primary_key=True, autoincrement=True)
    nome =  Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)

    def __init__(self, nome, email, senha, ativo):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
  
# livros
class Livro(Base):
    __tablename__ = "livros"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", Integer)
    qtd_paginas = Column("qtd_paginas", Integer)
    dono = Column("dono",ForeignKey('usuarios.id'))
    
    def __init__(self, titulo, qtd_paginas, dono):
        self.titulo = titulo
        self.qtd_paginas = qtd_paginas
        self.dono = dono

Base.metadata.create_all(bind=db) # cria todos as tabelas



# CRUD
# C- CREATE =====> Criando um item
# usuario = Usuario(nome='Sergio', email='sergiosemrebom@gmail.com', senha='123456', ativo=True)
# session.add(usuario) # adiciona o usuario na tabela
# session.commit() # fazendo o comit do usuario


# R - READ
usuario_sergio = session.query(Usuario).filter_by(email='sergiosemrebom@gmail.com').first() # a query faz uma consulta
print(usuario_sergio)
print(usuario_sergio.nome)
print(usuario_sergio.email)

#livro = Livro(titulo='Nome do Vento', qtd_paginas=100, dono=usuario_sergio.id)
#session.add(livro)
#session.commit()

# U - UPDATE
# usuario_sergio.nome = 'Sergio'
# session.add(usuario_sergio)
# session.commit()

# D - DELETE
session.delete(usuario_sergio)
session.commit()