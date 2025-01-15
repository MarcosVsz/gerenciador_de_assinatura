from sqlmodel import Field, SQLModel, Relationship
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

class Payments(SQLModel, table=True):
    id: int = Field(primary_key=True)
    subscription_id: int = Field(foreign_key='subscription.id')
    subscription: Subscription = Relationship()
    date: date