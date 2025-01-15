from sqlmodel import Field, SQLModel, create_engine
from typing import Optional
from datetime import date
from decimal import Decimal
#Transforma uma simples classe da linguagem python em uma tabela do banco de dados
class Subscription(SQLModel, table = True):
    id: int = Field(primary_key=True)#AutoIncrement Chave Primária
    empresa: str
    site: Optional[str] = None #O dado de colocar o site pode ser opcional, é importado da biblioteca uma "Função" que se o usuário nao colocar o dado que pede o site, continua funcionando por nao ser opcional.
    data_assinatura: date
    valor: Decimal #Poderia ser usado o Float, porém, poderia dar conflito devido as altas casas decimais existentes


#SQLite = banco de dados nativo do python
sqlite_file_name = 'databse.db'
#url de conexão com o banco de dados
sqlite_url = f'sqlite:///{sqlite_file_name}' #se estivesse mysql nao teria problema, continuaria funcionando

#Conexão do python e banco de dados, define tudo sobre o banco, é necessário!
engine = create_engine(sqlite_url, echo=True) #Echo: exite no terminal alguns dados de sql gerado ou algo do banco, após a finalização do desenvolvimento do software

if __name__ == '__main__':#variavel especial do python e sempre que roda o arquivo ele fala qual arquivo foi rodado. So executa a linha do if se tiver executando o arquivo por ele mesmo. Ex: python models/model.py
    SQLModel.metadata.create_all(engine)#Cria tudo que precisa ser criado na engine, dentro da tabela de banco de dados

'''
Comandos:
python -m venv venv
python models/model.py: executa o arquivo desejado
clear
pip install sqlmodel
venv\Scripts\Activate
'''