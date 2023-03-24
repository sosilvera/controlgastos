-- Insertar gastos, con las siguientes opciones:
	--- Monto
	--- Cuotas
	--- Intereses, y valor de la cuota
INSERT INTO Gastos (IdGasto, Descripcion, Monto, idBanco, FechaCompra, CuotasTotales, CuotasPagas, Intereses, ValorCuota, MesPrimeraCuota, MesUltimaCuota) VALUES
(1, 'Compra de muebles', 15000.00, 1, '2022-01-15', 12, 4, 1, 1500.00, 1, 3);

--- Ver consumos totales por mes
select idPeriodo, sum(monto) as Monto
from gasto_mes
group by idPeriodo;

--- Ver consumos totales por mes por tarjeta
select gm.idPeriodo, g.idBanco, sum(gm.Monto)
from gasto_mes gm
inner join gastos g
on g.idGasto = gm.idGasto
group by gm.idPeriodo, g.idBanco;

--- Ver consumos totales por tarjeta
select idBanco, sum(Monto) as totales
from Gastos
group by idBanco;

--- Ver consumos totales
select sum(Monto) as totales
from Gastos;
