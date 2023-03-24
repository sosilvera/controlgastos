from schema.models import Pedido_Estado, Pedido_Historico, Pedidos, db
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import urllib
from datetime import datetime
import commons.env as env

class Querys():
    def __init__(self):
        params = urllib.parse.quote_plus(env.STRING_CONNECTION)
        engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
        db.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)

        self.session = Session()
        
    def insertGasto(self, gasto):
        return

    def queryConsumosPorMes(self):
        return
    
    def queryTotalesPorMes(self):
        return

    def queryTotalesPorTarjetaMes(self):
        return

    def queryTotalesPorTarjeta(self):
        return

    def queryTotales(self):
        return
    
    def queryDeudaBCRA(self):
        return

    def insertPedidoEstado(self, idPedido, estado, ambiente, machine):
        p = Pedido_Estado(idPedido=idPedido, estado=estado, ambiente=ambiente, nombreMaquina=machine)
        self.session.add(p)
        self.session.commit()
    
    def getTask(self, idPedido):
        task = self.session.query(Pedidos).filter(Pedidos.idPedido == idPedido).first()
        return task
    

    def getTasks(self):
        tasks = self.session.query(Pedidos.idPedido, Pedidos.deployment, Pedidos.version, Pedidos.ambiente, Pedidos.variables,
                    Pedido_Estado.estado, Pedido_Estado.ambiente, Pedido_Estado.nombreMaquina)\
        .join(Pedido_Estado, Pedidos.idPedido == Pedido_Estado.idPedido)\
        .all()

        task_list = []
        
        for t in tasks:
            task = {
                "idPedido": str(t.idPedido),
                "deployment": t.deployment,
                "version": str(t.ambiente),
                "variables": str(t.variables),
                "estado": str(t.estado),
                "ambiente": str(t.nombreMaquina)
            }
            task_list.append(task)

        return task_list
    
    # Cierro la sesion de la base
    def sessionClose(self):
        self.session.close()