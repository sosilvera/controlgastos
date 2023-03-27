from schema.models import Bancos, Periodos, Gastos,DeudaBCRA,Gasto_Mes,db
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
        self.session.add(gasto)
        self.session.commit()
        return gasto.idGasto

    def insertGastoMes(self, idPrimeraCuota, idGasto, valorCuota, cantidadCuotas):
        for i in range(idPrimeraCuota, idPrimeraCuota+cantidadCuotas):
            cuota = Gasto_Mes(
                idGasto = idGasto,
                idPeriodo = i,
                monto = valorCuota
            )
            self.session.add(cuota)
        
        self.session.commit()

    def queryBancos(self):
        bancos = self.session.query(Bancos).all()
        return [{'id':banco.idBanco, 'nombre': banco.nombre} for banco in bancos]

    def queryConsumosPorMes(self):
        query = self.session.query(Gasto_Mes.idGastoMes,Periodos.descripcion, Gastos.descripcion, Gasto_Mes.monto, Bancos.nombre).\
            select_from(Gasto_Mes).\
            join(Gastos, Gastos.idGasto == Gasto_Mes.idGasto).\
            join(Bancos, Bancos.idBanco == Gastos.idBanco).\
            join(Periodos, Gasto_Mes.idPeriodo == Periodos.idPeriodo).\
            order_by(Gasto_Mes.idPeriodo)

        result = []
        for row in query.all():
            result.append({
                'periodo': row[0],
                'descripcion': row[1],
                'monto': row[2],
                'banco': row[3]
            })

        return result
    
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
    
    def queryPeriodoByMes(self, mes, anio):
        idPeriodo = self.session.query(Periodos.idPeriodo)\
            .filter(Periodos.NumeroMes == mes)\
            .filter(Periodos.NumeroAnio == anio)\
            .first()
        
        return idPeriodo[0]

    # Cierro la sesion de la base
    def sessionClose(self):
        self.session.close()

"""
    def insertPedidoEstado(self, idPedido, estado, ambiente, machine):
        p = Pedido_Estado(idPedido=idPedido, estado=estado, ambiente=ambiente, nombreMaquina=machine)
        self.session.add(p)
        self.session.commit()
    

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
"""
