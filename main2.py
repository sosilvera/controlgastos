from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from pydantic import BaseModel
from typing import List
from datetime import datetime

# Configuración de la base de datos
DATABASE_URL = "mssql+pyodbc://<usuario>:<contraseña>@<servidor>/<base_de_datos>?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Declaración de modelos
Base = declarative_base()

class Banco(Base):
    __tablename__ = "Bancos"

    IdBanco = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(100), index=True)

class Banco_Limite(Base):
    __tablename__ = "Banco_Limites"

    Id = Column(Integer, primary_key=True, index=True)
    IdBancoLimites = Column(Integer, ForeignKey("Bancos.IdBanco"))
    Limite_total = Column(Float)
    Limite_actual = Column(Float)

    banco = relationship("Banco", back_populates="limites")

class Periodo(Base):
    __tablename__ = "Periodos"

    IdPeriodo = Column(Integer, primary_key=True, index=True)
    Numero_Mes = Column(Integer)
    Numero_Anio = Column(Integer)

class DeudaBCRA(Base):
    __tablename__ = "DeudaBCRA"

    idDeuda = Column(Integer, primary_key=True, index=True)
    idBanco = Column(Integer, ForeignKey("Bancos.IdBanco"))
    Total = Column(Float)
    Situacion = Column(String(50))

    banco = relationship("Banco", back_populates="deudas")

class Gasto(Base):
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


class Gasto_Mes(Base):
    __tablename__ = "Gasto_Mes"

    IdGastoMes = Column(Integer, primary_key=True, index=True)
    idPeriodo = Column(Integer, ForeignKey("Periodos.IdPeriodo"))
    idGasto = Column(Integer, ForeignKey("Gastos.IdGasto"))
    Monto = Column(Float)

    periodo = relationship("Periodo", back_populates="gastos_mes")
    gasto = relationship("Gasto", back_populates="gastos_mes")

# Declaración de esquemas
class BancoSchema(BaseModel):
    IdBanco: int
    Nombre: str

    class Config:
        orm_mode = True

class BancoLimiteSchema(BaseModel):
    Id: int
    IdBancoLimites: int
    Limite_total: float
    Limite_actual: float
    banco: BancoSchema

    class Config:
        orm_mode = True

class PeriodoSchema(BaseModel):
    IdPeriodo: int
    Numero_Mes: int
    Numero_Anio: int

    class Config:
        orm_mode = True

class DeudaBCRASchema(BaseModel):
    idDeuda: int
    idBanco: int
    Total: float
    Situacion: str
    banco: BancoSchema

    class Config:
        orm_mode = True

class GastoSchema(BaseModel):
    IdGasto: int
    Descripcion: str
    Monto: float
    idBanco: int
    FechaCompra: str
    Cuotas_totales: int
    Cuotas_pagas: int
    Intereses: bool
    Valor_cuota: float
    Mes_primera_cuota: int
    Mes_ultima_cuota: int
    banco: BancoSchema
    mes_primera_cuota_rel: PeriodoSchema
    mes_ultima_cuota_rel: PeriodoSchema
    gastos_mes: List[Gasto_MesSchema] = []

    class Config:
        orm_mode = True

class GastoMesSchema(BaseModel):
    IdGastoMes: int
    idPeriodo: int
    idGasto: int
    Monto: float
    periodo: PeriodoSchema
    gasto: GastoSchema

    class Config:
        orm_mode = True

class GastoCreateSchema(BaseModel):
    Descripcion: str
    Monto: float
    idBanco: int
    FechaCompra: str = datetime.today().strftime('%Y-%m-%d')
    Cuotas_totales: int = 1
    Intereses: bool = False
    Valor_cuota: float = 0
    Mes_primera_cuota: int = None
    Mes_ultima_cuota: int = None

class GastoPagosSchema(BaseModel):
    Cuotas_totales: int
    Cuotas_pagas: int
    Intereses: bool
    Valor_cuota: float
    Mes_primera_cuota: int = None
    Mes_ultima_cuota: int = None

class GastoMesCreateSchema(BaseModel):
    idPeriodo: int
    idGasto: int
    Monto: float

# Configuración de la app
app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Conexión con la base de datos
SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://usuario:contraseña@nombre_servidor/nombre_base_datos?driver=SQL Server"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creación de las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Creación de un objeto de la clase DependencyInjection
di = DependencyInjection()

# Endpoint para crear un nuevo gasto
@app.post("/gastos", response_model=GastoSchema)
async def create_gasto(gasto: GastoCreateSchema):
    with di.get_db() as db:
        # Crear el objeto Gasto
        nuevo_gasto = Gasto(
            Descripcion=gasto.Descripcion,
            Monto=gasto.Monto,
            idBanco=gasto.idBanco,
            FechaCompra=gasto.FechaCompra,
            Cuotas_totales=gasto.Cuotas_totales,
            Cuotas_pagas=0,
            Intereses=gasto.Intereses,
            Valor_cuota=gasto.Valor_cuota,
            Mes_primera_cuota=gasto.Mes_primera_cuota,
            Mes_ultima_cuota=gasto.Mes_ultima_cuota,
        )
        # Agregar el gasto a la base de datos
        db.add(nuevo_gasto)
        db.commit()
        db.refresh(nuevo_gasto)
        return nuevo_gasto
