from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.models import Bancos, Banco_Limites, Periodos,DeudaBCRA, Gastos, Gasto_Mes
from schema.schemas import BancoSchema, BancoLimiteSchema, PeriodoSchema, DeudaBCRASchema, GastoSchema, GastoMesSchema, GastoCreateSchema
from commons.querys import Querys
import datetime

app = FastAPI()

# Configurar la conexión a la base de datos
q = Querys()

# Endpoint para crear un nuevo gasto
@app.get("/gasto")
async def get_gastos():
        gastos = q.queryGastos()
        return JSONResponse(content=gastos)

@app.post("/gasto")
async def create_gasto(gasto: GastoCreateSchema):

        # Obtener mes actual y sumarle 1
        mesActual = datetime.date.today().month
        idPrimeraCuota = q.queryPeriodoByMes(mesActual + 1, 2023)
        idUltimaCuota = idPrimeraCuota + gasto.cantidad_cuotas

        nuevo_gasto = Gastos(
                descripcion=gasto.descripcion,
                monto=gasto.monto,
                idBanco=gasto.idBanco,
                cuotasTotales=gasto.cantidad_cuotas,
                cuotasPagas=0,
                intereses=gasto.intereses,
                valorCuota=gasto.valor_cuota,
                MesPrimeraCuota=idPrimeraCuota,
                MesUltimaCuota=idUltimaCuota
        )
        
        # Agregar el gasto a la base de datos
        idGasto = q.insertGasto(nuevo_gasto)
        
        q.insertGastoMes(idPrimeraCuota, idGasto, gasto.valor_cuota, gasto.cantidad_cuotas)

        return nuevo_gasto

@app.get("/bancos")
async def bancos():
        bancos = q.queryBancos()
        return JSONResponse(content=bancos)

@app.get("/consumosMes")
async def consumosMes():
        consumos = q.queryConsumosPorMes()
        return JSONResponse(content=consumos)

@app.get("/totalesMesTarjeta")
async def consumosMesTarjeta():
        consumos = q.queryTotalesPorTarjetaMes()
        return JSONResponse(content=consumos)

@app.get("/totalesMesTarjeta")
async def totalesMesTarjeta():
        consumos = q.queryTotalesPorTarjetaMes()
        return JSONResponse(content=consumos)

@app.get("/totalesTarjeta")
async def totalesTarjeta():
        consumos = q.queryTotalesPorTarjeta()
        return JSONResponse(content=consumos)

@app.get("/totales")
async def totales():
        consumos = q.queryTotales()
        return JSONResponse(content=consumos)

@app.get("/deudabcra")
async def deuda():
        deuda = q.queryDeudaBCRA()
        return JSONResponse(content=deuda)