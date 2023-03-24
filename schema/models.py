from sqlalchemy import Boolean, Column , ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Banco(db.Model):
    __tablename__ = "Bancos"

    IdBanco = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(100), index=True)

class Banco_Limite(db.Model):
    __tablename__ = "Banco_Limites"

    Id = Column(Integer, primary_key=True, index=True)
    IdBancoLimites = Column(Integer, ForeignKey("Bancos.IdBanco"))
    Limite_total = Column(Float)
    Limite_actual = Column(Float)

    banco = relationship("Banco", back_populates="limites")

class Periodo(db.Model):
    __tablename__ = "Periodos"

    IdPeriodo = Column(Integer, primary_key=True, index=True)
    Numero_Mes = Column(Integer)
    Numero_Anio = Column(Integer)

class DeudaBCRA(db.Model):
    __tablename__ = "DeudaBCRA"

    idDeuda = Column(Integer, primary_key=True, index=True)
    idBanco = Column(Integer, ForeignKey("Bancos.IdBanco"))
    Total = Column(Float)
    Situacion = Column(String(50))

    banco = relationship("Banco", back_populates="deudas")

class Gasto(db.Model):
    __tablename__ = "Gastos"

    IdGasto = Column(Integer, primary_key=True, index=True)
    Descripcion = Column(String(100))
    Monto = Column(Float)
    idBanco = Column(Integer, ForeignKey("Bancos.IdBanco"))
    FechaCompra = Column(String(10), default=datetime.today().strftime('%Y-%m-%d'))
    Cuotas_totales = Column(Integer, default=1)
    Cuotas_pagas = Column(Integer, default=0)
    Intereses = Column(Boolean, default=False)
    Valor_cuota = Column(Float, default=0)
    Mes_primera_cuota = Column(Integer, ForeignKey("Periodos.IdPeriodo"))
    Mes_ultima_cuota = Column(Integer, ForeignKey("Periodos.IdPeriodo"))

    banco = relationship("Banco", back_populates="gastos")
    mes_primera_cuota_rel = relationship("Periodo", foreign_keys=[Mes_primera_cuota])
    mes_ultima_cuota_rel = relationship("Periodo", foreign_keys=[Mes_ultima_cuota])

class Gasto_Mes(db.Model):
    __tablename__ = "Gasto_Mes"

    IdGastoMes = Column(Integer, primary_key=True, index=True)
    idPeriodo = Column(Integer, ForeignKey("Periodos.IdPeriodo"))
    idGasto = Column(Integer, ForeignKey("Gastos.IdGasto"))
    Monto = Column(Float)

    periodo = relationship("Periodo", back_populates="gastos_mes")
    gasto = relationship("Gasto", back_populates="gastos_mes")