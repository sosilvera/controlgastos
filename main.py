from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.models import Banco, Banco_Limite, Periodo,DeudaBCRA, Gasto, Gasto_Mes
from schema.schemas import BancoSchema, BancoLimiteSchema, PeriodoSchema, DeudaBCRASchema, GastoSchema, GastoMesSchema, GastoCreateSchema
from commons.querys import Querys


app = FastAPI()

# Configurar la conexión a la base de datos
q = Querys()

# Endpoint para crear un nuevo gasto
@app.post("/gasto")
async def create_gasto(gasto: GastoCreateSchema):

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
    q.insertGasto(nuevo_gasto)
    
    return nuevo_gasto