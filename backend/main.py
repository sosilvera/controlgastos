from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from schema.models import Bancos, Banco_Limites, Periodos,DeudaBCRA, Gastos, Gasto_Mes
from schema.schemas import BancoSchema, BancoLimiteSchema, PeriodoSchema, DeudaBCRASchema, GastoSchema, GastoMesSchema, GastoCreateSchema
from commons.querys import Querys
import utils.graphics as gh
import datetime

app = FastAPI()

# Agregar CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
        consumosJson = JSONResponse(content=consumos)
        gh.plot_evolucion_gastos(consumos)
        return consumosJson

@app.get("/totalesMesTarjeta") # Devuelve NULL
async def consumosMesTarjeta():
        mesActual = datetime.date.today().month
        periodo = q.queryPeriodoByMes(mesActual + 1, 2023)
        
        consumos = q.queryTotalesPorTarjetaProximoMes(periodo)
        return JSONResponse(content=consumos)

@app.get("/totalesTarjeta")
async def totalesTarjeta():
        consumos = q.queryTotalesPorTarjeta()
        return JSONResponse(content=consumos)

@app.get("/totales") # Devuelve NULL
async def totales():
        consumos = q.queryTotales()
        return JSONResponse(content=consumos)

@app.get("/deudabcra") # Devuelve NULL
async def deuda():
        deuda = q.queryDeudaBCRA()
        deudaJson = JSONResponse(content=deuda)
        return deudaJson

@app.get('/gastoProximoMes')
async def proximoMes():
        mesActual = datetime.date.today().month
        periodo = q.queryPeriodoByMes(mesActual + 1, 2023)
        total = q.queryTotalByPeriodo(periodo)
        return JSONResponse(total)
