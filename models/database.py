from sqlmodel import Field, SQLModel, create_engine
from .model import *

#SQLite = banco de dados nativo do python
sqlite_file_name = 'databse.db'
#url de conexão com o banco de dados
sqlite_url = f'sqlite:///{sqlite_file_name}' #se estivesse mysql nao teria problema, continuaria funcionando

#Conexão do python e banco de dados, define tudo sobre o banco, é necessário!
engine = create_engine(sqlite_url, echo=False) #Echo: exite no terminal alguns dados de sql gerado ou algo do banco, após a finalização do desenvolvimento do software

if __name__ == '__main__':#variavel especial do python e sempre que roda o arquivo ele fala qual arquivo foi rodado. So executa a linha do if se tiver executando o arquivo por ele mesmo. Ex: python models/model.py
    SQLModel.metadata.create_all(engine)#Cria tudo que precisa ser criado na engine, dentro da tabela de banco de dados
