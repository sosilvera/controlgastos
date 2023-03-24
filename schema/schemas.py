from pydantic import BaseModel
from datetime import datetime

# Declaración de esquemas
class BancoSchema(BaseModel):
    IdBanco: int
    Nombre: str
    
class BancoLimiteSchema(BaseModel):
    Id: int
    IdBancoLimites: int
    Limite_total: float
    Limite_actual: float
    banco: BancoSchema

class PeriodoSchema(BaseModel):
    IdPeriodo: int
    Numero_Mes: int
    Numero_Anio: int

class DeudaBCRASchema(BaseModel):
    idDeuda: int
    idBanco: int
    Total: float
    Situacion: str
    banco: BancoSchema


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

class GastoMesSchema(BaseModel):
    IdGastoMes: int
    idPeriodo: int
    idGasto: int
    Monto: float
    periodo: PeriodoSchema
    gasto: GastoSchema


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


