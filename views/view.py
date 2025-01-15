import __init__

from models.database import engine
from models.model import Subscription, Payments
from sqlmodel import Session, select
from datetime import date

class SubscriptionService:
    def __init__(self, engine):
        self.engine = engine
    #recebe dados de uma inscrição e salva no banco de dados
    def create(self, subscription: Subscription):#def cria o subscription em dados salvos no banco de dados
        with Session(self.engine) as session: #gerenciador de contextos no python
            session.add(subscription)#salva as coisas no banco de dados
            session.commit()
            return subscription
    def list_all(self):
        with Session(self.engine) as session:
            statement = select(Subscription)#metodo responsavel por buscar informações do banco
            results = session.exec(statement).all()
        return results
    
    def _has_pay(self, results):
        for result in results: 
            if result.date.month == date.today().month:
                return True
        return False

    def pay(self, subscription: Subscription):
        with Session(self.engine) as session:
            statement = select(Payments).where(Subscription.empresa==subscription.empresa)
            results = session.exec(statement).all()
            
            if self._has_pay(results):
                question = input('Essa conta ja foi paga esse mês, deseja pagar novamente? Y ou N: ')

                if not question.upper() == 'Y':
                    return
                
            pay = Payments(subscription_id=subscription.id, date=date.today())
            session.add(pay)
            session.commit()


ss = SubscriptionService(engine)
subscription = Subscription(empresa='Hbo Max', site='hbo.com.br', data_assinatura=date.today(), valor=8) #instancia da classe subscription
ss.pay(subscription)